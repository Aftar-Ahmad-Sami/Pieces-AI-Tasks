from pieces_copilot_sdk import PiecesClient
import streamlit as st

def hello_world():
    """
    This function demonstrates the usage of the Pieces CoPilot SDK.
    It creates a conversation with the PiecesClient and displays the response in a Streamlit app.

    The function performs the following steps:
    1. Initializes a PiecesClient instance with the specified base URL.
    2. Sets the title of the Streamlit app.
    3. Provides a text input box for the user to enter a question.
    4. Creates a conversation using the PiecesClient with the user's input as the first message.
    5. Displays the response from the conversation in the Streamlit app.

    Returns:
        None
    """
    # Create an instance of PiecesClient
    pieces_client = PiecesClient(
        config={
            'baseUrl': 'http://localhost:1000'
        }
    )

    st.title("Pieces CoPilot SDK Trial")

    # Input text input box
    query = st.text_input("Enter your question here:")
    conversation_response = pieces_client.create_conversation(
        props={
            "name": "Test Conversation",
            "firstMessage": query
        }
    )
    st.write(conversation_response['answer']['text'])
hello_world()
