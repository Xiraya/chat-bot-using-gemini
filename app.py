import os
import textwrap
from IPython.display import display
from IPython.display import Markdown
import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyAwuVTBm8qQnV4aJL-KbElV2jTvQOZC7aQ')
tmodel = genai.GenerativeModel('gemini-pro')
imodel = genai.GenerativeModel('gemini-pro-vision')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])
st.title('Welcome to Chat assistant')

def role_to_streamlit(role):
    if role=='model':
        return 'assistant'
    else:
         return role
    
def get_gemini_response(input,image):
    if input!="" and image!="":
       response = imodel.generate_content([input,image])
    elif image!="" and text=="":
        response=imodel.generate_content(image)
    else:
       response = tmodel.generate_content(input)
    return response.text

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)
   
        
if prompt := st.chat_input("What can I do for you?") or image := st.file_uploader("upload an image", type=['jpg','jpeg','png']):
    st.chat_message('user').markdown(prompt)
    response = st.session_state.chat.send_message(prompt) 
    
    with st.chat_message("assistant"):
	    st.markdown(response.text)