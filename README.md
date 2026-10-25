# Ollama Docker Chatbot

A simple chatbot built with Streamlit and Ollama, powered by the
`mistral:latest` model, with Docker support.

<img src="https://raw.githubusercontent.com/abhishek-Jain24/ollama-docker-chatbot/12d2ac0a1c483eb20f14f26eb739c8ffd281b98a/Screenshot%202026-10-25%20111218.png" alt="Ollama Docker Chatbot Screenshot" width="800">

## Features

- Simple chat interface
- Local model inference using Ollama
- Session-based chat history
- Environment-based configuration
- Docker support
- No OpenAI API key required for local usage

## Tech Stack

- Python
- Streamlit
- Ollama
- Mistral
- Docker
- uv
- python-dotenv

## Project Structure

```text
ollama-docker-chatbot/
├── .dockerignore
├── .env.example
├── .gitignore
├── .python-version
├── app.py
├── commands.txt
├── Dockerfile
├── README.md
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

Create `.env` locally. Do not upload it to GitHub.
The commands file may have a different name in your project.

## Prerequisites

- Python compatible with `pyproject.toml`
- uv
- Ollama installed and running
- Docker Desktop for running the app in a container

## Run Locally

### 1. Get the project

Clone this repository using its GitHub URL, or download and extract
the ZIP file. Open a terminal in the project folder.

### 2. Download the model

```bash
ollama pull mistral:latest
```

Check installed models:

```bash
ollama list
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Create a `.env` file

Create `.env` in the project root:

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral:latest
```

### 5. Start the app

Make sure Ollama is running, then run:

```bash
uv run streamlit run app.py
```

Open the URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## Run with Docker

In this setup, the Streamlit app runs inside Docker.
Ollama and the Mistral model run separately on your computer.

The commands below assume the Dockerfile installs the required
dependencies and starts Streamlit on `0.0.0.0:8501`.

### 1. Configure the connection

For Docker Desktop on Windows or macOS, set `.env` to:

```env
OLLAMA_HOST=http://host.docker.internal:11434
OLLAMA_MODEL=mistral:latest
```

### 2. Build the image

Run from the folder containing the Dockerfile:

```bash
docker build -t ollama-docker-chatbot .
```

### 3. Run the container

```bash
docker run --rm -p 8501:8501 --env-file .env ollama-docker-chatbot
```

### 4. Open the chatbot

```text
http://localhost:8501
```

Keep Ollama running on your computer.

On Linux Docker Engine, connecting to a host-based Ollama server
may require additional networking configuration.

## How It Works

```text
User
  |
  v
Streamlit Chat Interface
  |
  v
Ollama Server
  |
  v
mistral:latest
  |
  v
Reply Displayed in Streamlit
```

1. The user enters a message.
2. The app adds it to the session's chat history.
3. The conversation is sent to Ollama.
4. Mistral generates a reply.
5. The reply is displayed and added to the chat history.

## Chat History

The app stores messages temporarily in `st.session_state`.

Previous messages are sent with each request so the model can
use the conversation as context.

There is no database or permanent conversation storage.
Session history is not long-term model memory.

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `OLLAMA_HOST` | Ollama server address | `http://localhost:11434` |
| `OLLAMA_MODEL` | Model used for replies | `mistral:latest` |

Use the local address when running directly on your computer.
Use the Docker Desktop host address when the app runs in a container
and Ollama runs on your computer.

## Why Docker?

Docker packages the app and its dependencies into an isolated
environment, making the setup easier to reproduce and share.

It does not automatically install Ollama or download the model
onto another person's computer.

## Troubleshooting

### Missing Python module

Install the project dependencies and run through uv:

```bash
uv sync
uv run streamlit run app.py
```

### Cannot connect to Ollama

- Check that Ollama is running.
- Check `OLLAMA_HOST` in `.env`.
- Check that the model is installed with `ollama list`.
- Restart the Streamlit app after changing environment settings.

### Model not found

```bash
ollama pull mistral:latest
```

### Slow responses

Response speed depends on the model and available CPU, GPU, and RAM.

## Security

- Do not commit `.env`.
- Do not include `.env` in the Docker image.
- Keep `.env` in both `.gitignore` and `.dockerignore`.
- Share configuration examples through `.env.example`.
- Do not expose your local Ollama server publicly without
  appropriate access controls.

## Project Purpose

This project demonstrates a simple local AI chatbot and how to
package a Python application using Docker.
