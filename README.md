# AI-Chatbot (LangChain + Streamlit + Ollama)

A minimal chatbot UI built with Streamlit that uses LangChain to prompt a local LLM served by Ollama (default model: `llama2`).

## Features
- Simple Streamlit interface to ask questions
- Local inference via Ollama (no cloud required)
- LangChain prompt and LCEL chaining

## Prerequisites
- Python 3.10+
- Ollama installed and running locally

### Install Ollama (Linux)
```bash
curl -fsSL https://ollama.com/install.sh | sh

# Start the Ollama server (in a terminal)
ollama serve

# Download the model used by this app
ollama pull llama2
```

Tip: Keep `ollama serve` running while you use the app. By default, it listens on `http://localhost:11434`.

## Setup
```bash
# Optional: create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment variables (optional)
This project can emit LangChain tracing to LangSmith. If you are not using LangSmith, disable tracing or leave the API key empty.

Create or edit a `.env` file in the project root with:
```dotenv
# Disable if you are not using LangSmith
LANGCHAIN_TRACING_V2=false

# Only needed if LANGCHAIN_TRACING_V2=true and you have a LangSmith account
LANGCHAIN_API_KEY=

# Optional project label
LANGCHAIN_PROJECT=AI-Chatbot
```
## Project Structure
```
README.md
requirements.txt
AI-Chatbot/
	main.py
.env  # local env vars (do not commit secrets)
```

## Run
Ensure Ollama is running and the `llama2` model is available, then start Streamlit:
```bash
streamlit run AI-Chatbot/main.py
```

This opens a local app in your browser. Enter a question and the chatbot will respond using the local `llama2` model via Ollama.

## Troubleshooting
- Cannot connect to Ollama (connection refused at `localhost:11434`):
	- Start the server: `ollama serve`
	- Confirm it’s up: `curl http://localhost:11434/api/tags`
- Model not found: Run `ollama pull llama2` (or your chosen model).
- Streamlit port in use: Run on a different port:
	```bash
	streamlit run AI-Chatbot/main.py --server.port 8502
	```
- LangChain tracing warnings:
	- Set `LANGCHAIN_TRACING_V2=false` in `.env`, or
	- Provide a valid `LANGCHAIN_API_KEY` if you use LangSmith.

### Happy Learning :)