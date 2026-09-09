# Chatbot with LangGraph

A basic chatbot project built in Python using LangGraph and LangChain. The application creates a graph with one node responsible for sending user messages to an OpenAI model and displaying the responses in the terminal.

## Technologies

- Python
- LangGraph
- LangChain
- OpenAI
- python-dotenv

## Setup

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-key-here
   ```

## Running the Application

With the virtual environment activated, run:

```bash
python project-chatbot.py
```

Enter a message to chat with the bot. The chatbot remembers the questions and
answers from the current terminal session. To exit, type `exit`.

The memory is kept in process using LangGraph's `MemorySaver`, so it is reset
when the application is restarted.

## Project Structure

- `project-chatbot.py`: graph implementation and conversation loop.
- `requirements.txt`: project dependencies.
- `.env`: local API key configuration, ignored by Git.
