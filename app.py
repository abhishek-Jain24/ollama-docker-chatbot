# """A tiny Streamlit chatbot used to demonstrate Docker.

# The app reads OPENAI_API_KEY and OPENAI_MODEL from the environment.
# Locally, python-dotenv loads them from a .env file.
# In Docker, pass that file at startup with --env-file. It is not copied
# into the image.
# """

# import os

# import streamlit as st
# from dotenv import load_dotenv
# from openai import OpenAI


# # Load a local .env file when one exists. Variables already set in the
# # environment are kept, so a key passed with --env-file is not replaced.
# load_dotenv()

# st.set_page_config(page_title="GenAI Chatbot")
# st.title("GenAI Chatbot")
# st.write(
#     "A simple chatbot for a Docker lesson. "
#     "Your message and the chat history are sent to an OpenAI model, "
#     "and the reply is shown below."
# )

# api_key = os.getenv("OPENAI_API_KEY", "").strip()
# model = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"

# st.caption(f"Model: {model}")

# if not api_key or api_key == "your_openai_api_key_here":
#     st.error(
#         "No OpenAI API key found. Copy .env.example to .env, paste your key "
#         "into OPENAI_API_KEY, and start the app again. When you use Docker, "
#         "pass that file at runtime with --env-file .env."
#     )
#     st.stop()

# # session_state keeps the conversation for this browser tab.
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# user_message = st.chat_input("Type a message")
# if not user_message:
#     st.stop()

# st.session_state.messages.append({"role": "user", "content": user_message})
# with st.chat_message("user"):
#     st.markdown(user_message)

# client = OpenAI(api_key=api_key)

# try:
#     with st.spinner("Waiting for the model..."):
#         response = client.chat.completions.create(
#             model=model,
#             messages=[
#                 {
#                     "role": "system",
#                     "content": (
#                         "You are a helpful assistant in a beginner Docker and "
#                         "GenAI class. Keep answers clear and short."
#                     ),
#                 },
#                 *st.session_state.messages,
#             ],
#         )
#     answer = response.choices[0].message.content or "(The model returned an empty reply.)"
# except Exception as error:
#     st.error(
#         "The OpenAI request failed. Check the API key, the model name, "
#         f"and your network connection.\n\nDetails: {error}"
#     )
#     st.stop()

# with st.chat_message("assistant"):
#     st.markdown(answer)

# st.session_state.messages.append({"role": "assistant", "content": answer})


"""#######################################################################################"""

"""A simple Streamlit chatbot using local Ollama."""

import os

import streamlit as st
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

st.set_page_config(page_title="Ollama Chatbot")
st.title("Ollama Chatbot")
st.write("Apne local Ollama model se baat karo.")

# Read settings from .env
host = os.getenv("OLLAMA_HOST", "").strip() or "http://localhost:11434"
model = os.getenv("OLLAMA_MODEL", "").strip() or "mistral:latest"

st.caption(f"Model: {model}")

client = Client(host=host)

# Keep chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Type a message")

if not user_message:
    st.stop()

st.session_state.messages.append(
    {"role": "user", "content": user_message}
)

with st.chat_message("user"):
    st.markdown(user_message)

try:
    with st.spinner("Waiting for the model..."):
        response = client.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant in a beginner Docker "
                        "and GenAI class. Keep answers clear and short."
                    ),
                },
                *st.session_state.messages,
            ],
        )

        answer = (
            response.message.content
            or "(The model returned an empty reply.)"
        )

except Exception as error:
    st.error(
        "Ollama se connection nahi hua. Check karo ki Ollama "
        "running hai aur model ka naam sahi hai."
    )
    st.code(str(error))
    st.stop()

with st.chat_message("assistant"):
    st.markdown(answer)

st.session_state.messages.append(
    {"role": "assistant", "content": answer}
)