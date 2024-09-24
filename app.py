from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
import streamlit as st



#FUNCTION TO LOAD gemini
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

    ##initialize our streamlit app

st.set_page_config(page_title="Chatbot using Gemini")
st.header("Gemini Chatbot")

input=st.text_input("Input: ",key="input")

submit=st.button("Ask the Question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("Chatbot")
    st.write(response)