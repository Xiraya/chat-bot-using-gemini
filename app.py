import streamlit as st
from streamlit_option_menu import option_menu
import os
import textwrap
from IPython.display import display
from IPython.display import Markdown
import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key='AIzaSyAwuVTBm8qQnV4aJL-KbElV2jTvQOZC7aQ')


with st.sidebar:
    selected= option_menu(
        menu_title=None,
        options=['Text to Text','Image to Text','About'],
        icons=['keyboard','image','info-circle'],
        default_index=0
    )

if selected=='Text to Text':
  model = genai.GenerativeModel('gemini-pro')

  if "chat" not in st.session_state:
      st.session_state.chat = model.start_chat(history = [])
  st.title('Welcome to IT Chat Support.💻🔎')

  def role_to_streamlit(role):
      if role=='model':
          return 'assistant'
      else:
          return role

  for message in st.session_state.chat.history:
      with st.chat_message(role_to_streamlit(message.role)):
          st.markdown(message.parts[0].text)
          
  if prompt := st.chat_input("What is your query?"):
      st.chat_message('user').markdown(prompt)
      response = st.session_state.chat.send_message(prompt) 
      
      with st.chat_message("assistant"):
        st.markdown(response.text)

if selected == 'Image to Text':
  model = genai.GenerativeModel('gemini-pro-vision')

  #if "chat" not in st.session_state:
    #st.session_state.chat = model.start_chat(history=[])

  st.title('Welcome to Chat Support.💻🔎')

  def role_to_streamlit(role):
      if role == 'model':
          return 'assistant'
      else:
          return role

  def get_gemini_response(input,image):
      if input!="":
        response = model.generate_content([input,image])
      else:
        response = model.generate_content(image)
      return response.text

  #for message in st.session_state.chat.history:
      # with st.chat_message(role_to_streamlit(message.role)):
      #     st.markdown(message.parts[0].text)


  uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'], key="file_uploader")


  if prompt := st.chat_input("What is your query?"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        st.chat_message('user').markdown(prompt)

        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        image_bytes = image_bytes.getvalue()

        response = get_gemini_response(prompt,image)  # Assuming send_message can handle bytes

        with st.chat_message("assistant"):
            st.markdown(response)
            
if selected == "About":
    st.title("Chat bot for IT support  🐥")
    st.image('Cipher thugs.jpeg', caption='Cipher thugs 👾')
    st.subheader('DEVELOPED BY')
    st.markdown(
        """
        
        - 🧑‍💻Srivarsen R 
        - 🧑‍💻Shyam TR 
        - 🧑‍💻Nakulan T 
        
         
        
        """
    )
    st.markdown("                                 ")
    st.subheader("LANGUAGE USED : ")
    st.markdown("""- Python
                """)
    st.markdown("                                 ")

    git='https://github.com/TRshyam/hackathon'
    st.subheader("🤖[Click here for Project Source code](%s)🤖"%git)


    st.caption("Thank you for visiting this page 🤓")
