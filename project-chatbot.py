from langgraph.graph import StateGraph
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_openai  import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
# Load local environment variables, including the OpenAI API key.
load_dotenv(find_dotenv(), override=True)

# Define the state shared between the graph nodes.
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Create a graph builder that uses the state defined above.
graph_builder = StateGraph(State)

# Initialize the language model used to generate chatbot responses.
llm = ChatOpenAI(model="gpt-5-nano")

def chatbot(state: State):
    # Send the current messages to the model and return its response.
    response = llm.invoke(state["messages"])
    return {
        "messages": [response]
    }

# Register the chatbot node and define the graph's entry and exit points.
graph_builder.add_node("chatbot", chatbot)
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")

# Compile the graph into an executable application.
graph = graph_builder.compile()

# Display visual and text representations of the graph for inspection.
from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))
print(graph.get_graph().draw_ascii())

# Keep the terminal conversation running until the user types "exit".
while True:
    user_input = input("User: ")
    if (user_input.lower() == "exit"):
        print ("Exiting the chatbot.")
        break

    # Stream graph updates and print each generated response.
    for event in graph.stream(
        {"messages": [("user", user_input)]},
        stream_mode="updates"
    ):
        for value in event.values():
            message = value["messages"][-1]
            print(f"Chatbot: {message.content}")
            print("-" * 50)