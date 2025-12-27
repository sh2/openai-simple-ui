import streamlit as st
from openai import OpenAI
from typing import cast, get_args, Literal

ReasoningEffort = Literal["high", "medium", "low", "minimal", "none"]
Verbosity = Literal["high", "medium", "low"]


def main():
    st.set_page_config(page_title="OpenAI Simple UI")
    st.title("OpenAI Simple UI")

    with st.sidebar:
        new_chat = st.button("New chat")
        st.title("Settings")
        model_options = ["gpt-5.2", "gpt-5.2-chat-latest"]
        model = st.selectbox("Model", model_options, index=0)
        reasoning_effort = st.selectbox(
            "Reasoning effort", get_args(ReasoningEffort), index=1)
        verbosity = st.selectbox("Verbosity", get_args(Verbosity), index=1)

    if new_chat or "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask anything"):
        messages = []
        response = ""
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_assistant = st.empty()

        for message in st.session_state.messages:
            messages.append(message)

        client = OpenAI()

        for response_chunk in client.chat.completions.create(
            model=model,
            messages=messages,
            reasoning_effort=cast(ReasoningEffort, reasoning_effort),
            verbosity=cast(Verbosity, verbosity),
            stream=True,
        ):
            if response_chunk.choices:
                response += response_chunk.choices[0].delta.content or ""
                message_assistant.markdown(response + "▌")

        message_assistant.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
