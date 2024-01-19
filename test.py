import os
import textwrap
from IPython.display import display
from IPython.display import Markdown
import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyAwuVTBm8qQnV4aJL-KbElV2jTvQOZC7aQ')
model = genai.GenerativeModel('gemini-pro')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title('Welcome to Chat assistant')

def role_to_streamlit(role):
    if role == 'model':
        return 'assistant'
    else:
        return role

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("What can I do for you?"):
    st.chat_message('user').markdown(prompt)

    # Check if the user uploaded an image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # You can now process the uploaded image, for example, by sending it to the model
        # and displaying the response
        # image_processing_code(uploaded_image)
        
        # For demonstration purposes, let's just display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # You can then send a message to the chatbot with details about the uploaded image
        response = st.session_state.chat.send_message("User uploaded an image")

        with st.chat_message("assistant"):
            st.markdown(response.text)
    else:
        response = st.session_state.chat.send_message(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.text)
