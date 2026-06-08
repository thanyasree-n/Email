import google.generativeai as genai
import streamlit as st
genai.configure(api_key="enter the API key here")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("EMail!")
prompt=st.text_input("Can you write an email?")
if st.button("submit"):
    response=model.generate_content(prompt+"You are a Smart Email Writer Assistant specialized in writing, replying to, and improving emails; generate professional and context-aware emails, create email replies, adjust tone (Professional, Formal, Friendly, Casual, Polite, Persuasive, Apologetic, or Confident), format responses with Subject, Greeting, Body, and Closing when applicable, improve grammar and clarity, provide quick email responses, and if a request is not related to email writing, replying, or email improvement, respond exactly with: 'I am sorry, I can only answer email writing and email-related questions.'"
)
    st.write(response.text)