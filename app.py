from dotenv import load_dotenv
load_dotenv() #Loading all env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function to load Gemini Flash Model and Get Responses
model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#Initialize Streamlit App
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
inputs=st.text_input("input: ",key="input")
submit=st.button("Ask the question")

#Action when submit button is clicked
if submit:
    response=get_gemini_response(inputs)
    st.subheader("The Response is")
    st.write(response)
