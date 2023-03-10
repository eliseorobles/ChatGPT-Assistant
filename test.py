import streamlit as st
from pathlib import Path
from ml_model import ml_backend
from streamlit.components.v1 import html
from utils import *
from io import StringIO
import base64
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#to handle images
f_path = Path().absolute()
header_path = f_path/'header.png'
background_path = f_path/'background.png'

st.markdown("<h1 style='text-align: center;'>Open Ai Chatbot</h1>", unsafe_allow_html=True)



def add_header_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <h3 style="text-align: center;"><img src='data:image/{"png"};base64,{encoded_string.decode()}'/>Text Heading
    </h3>
    """,
    unsafe_allow_html=True
    )
add_header_from_local(header_path)    
st.markdown(description, unsafe_allow_html=True)

b = ml_backend()

col1, col2, col3 = st.columns(3)


# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = "Tell me what to do"

with col1:



    with st.form(key="form1"):
        st.markdown(f'<h3 style="background-color:#addff0;text-align: center;">Generate Email</h3>', unsafe_allow_html=True)


        st.markdown(""" 

   * Time saved writing medium-long sized emails
   * Mental Energy is conserved
   * Anxiety of writing a **professional sounding** email (or email with any writing style) is removed as the GPT3 Language model used is trained from a variety of many different internet sources

    """)
        prompt = st.text_input("Describe the Kind of Email you want to be written.")
        st.text(f"(Example: Write me a professional sounding email to my boss)")

        start = st.text_input("Begin writing the first few or several words of your email:")

        slider = st.slider("How many characters do you want your email to be? ", min_value=64, max_value=750)
        st.text("(A typical email is usually 100-500 characters)")

        submit_button = st.form_submit_button(label='Generate Email')

        if submit_button:
            with st.spinner("Generating Email..."):
                output = b.generate_email(prompt, slider)
            st.markdown("## Email Output:")
            st.markdown(start + output)

 


#Generate Email, Generate Code Info, Generate Documentation

with col2:
   
   with st.form(key="form2"):
        st.markdown(f'<h3 style="background-color:#9ceb91;text-align: center;">Generate Code Info</h3>', unsafe_allow_html=True)
        st.markdown("""
        * GPTs ability create and understand code allows us to use it to perform tasks like explaining what the code in a file does""")

        prompt = st.text_area("Pate the code that needed explanations.")
       

        submit_button = st.form_submit_button(label='Generate Code Info')
 
        if submit_button:
            with st.spinner("Generating Result..."):
                output = b.generate_codeinfo(prompt)
            st.markdown("## Output:")
            st.subheader(output)

   

with col3:
   
    with st.form(key="form3"):
        st.markdown(f'<h3 style="background-color:#f5b16e;text-align: center;">Generate Documentation</h3>', unsafe_allow_html=True)



        prompt = st.text_area("Place the document that need to be improved")

        uploaded_file = st.file_uploader("or choose a file")



        submit_button = st.form_submit_button(label='Generate Documentation')

        if submit_button:
            with st.spinner("Improving Documentation"):

                if prompt:
                    output, tech = b.generate_document(prompt)
                elif uploaded_file:
                    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                    
                    output, tech = b.generate_document(stringio.read())
                    
            st.markdown("## Output")

            st.markdown(output)
            
            st.markdown(f"1{tech}")



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local(background_path)    
    