import streamlit as st
from pieces_copilot_sdk import PiecesClient

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

st.title("Pieces CoPilot Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "Hello! How can I help you today?"}]

if "conversation_id" not in st.session_state:
    conversation = pieces_client.create_conversation(props={"name": "Streamlit Conversation"})
    st.session_state.conversation_id = conversation["conversation"].id

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Type a message...")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    response = pieces_client.prompt_conversation(
        message=query,
        conversation_id=st.session_state.conversation_id
    )

    with st.chat_message("assistant"):
        st.markdown(response["text"])

    st.session_state.messages.append({"role": "assistant", "content": response["text"]})
