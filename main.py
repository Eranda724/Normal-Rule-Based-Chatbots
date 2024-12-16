import streamlit as st
import json

# Load intents file or chatbot data
def load_intents(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Simple chatbot response function
def chatbot_response(user_input, intents):
    for intent in intents['intents']:
        if user_input.lower() in intent['patterns']:
            return intent['responses'][0]
    return "I can't understand what you're saying."

# Streamlit application
def main():
    st.title("Chatbot Application")
    st.write("Welcome to the chatbot! Ask me anything.")

    # Load intents
    intents_file = "data.json"  # Replace with your intents file path
    intents = load_intents(intents_file)

    # Chat interface
    user_input = st.text_input("You:", key="user_input")
    
    if user_input:
        response = chatbot_response(user_input, intents)
        st.text_area("Chatbot:", value=response, height=100)

if __name__ == '__main__':
    main()
