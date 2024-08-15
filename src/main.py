import streamlit as st
from pieces_copilot_sdk import PiecesClient

# Initialize the PiecesClient with the given configuration
pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

# Set the title of the Streamlit app
st.title("Pieces CoPilot Chatbot")

# Initialize the session state for messages if it doesn't exist
if "messages" not in st.session_state:
    # Default message from the bot when the session starts
    st.session_state.messages = [{"role": "bot", "content": "Hello! How can I help you today?"}]

# Initialize the session state for conversation_id if it doesn't exist
if "conversation_id" not in st.session_state:
    # Create a new conversation using the PiecesClient
    conversation = pieces_client.create_conversation(props={"name": "Streamlit Conversation"})
    # Store the conversation ID in the session state
    st.session_state.conversation_id = conversation["conversation"].id

# Display all messages stored in the session state
for message in st.session_state.messages:
    # Display each message in the chat interface
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for the user to type a message
query = st.chat_input("Type a message...")

# If the user has entered a message
if query:
    # Display the user's message in the chat
    with st.chat_message("user"):
        st.markdown(query)
    # Append the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": query})

    # Get the response from the PiecesClient by prompting the conversation
    response = pieces_client.prompt_conversation(
        message=query,
        conversation_id=st.session_state.conversation_id
    )

    # Display the assistant's response in the chat
    with st.chat_message("assistant"):
        st.markdown(response["text"])

    # Append the assistant's response to the session state
    st.session_state.messages.append({"role": "assistant", "content": response["text"]})
