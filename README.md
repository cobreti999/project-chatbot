# Chatbot com LangGraph

Projeto básico de chatbot desenvolvido em Python usando LangGraph e LangChain. A aplicação cria um grafo com um nó responsável por enviar as mensagens do usuário para um modelo da OpenAI e exibir as respostas no terminal.

## Tecnologias

- Python
- LangGraph
- LangChain
- OpenAI
- python-dotenv

## Configuração

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:

   ```env
   OPENAI_API_KEY=sua-chave-aqui
   ```

## Execução

Com o ambiente virtual ativo, execute:

```bash
python project-chatbot.py
```

Digite uma mensagem para conversar com o chatbot. Para encerrar, digite `exit`.

## Estrutura básica

- `project-chatbot.py`: implementação do grafo e do loop de conversação.
- `requirements.txt`: dependências do projeto.
- `.env`: configuração local da chave da API, não versionada pelo Git.
