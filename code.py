import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6IfcUWgaQDbndViKLLYg1YK_EOmfkop3IyfwXzk7Vi0wQx")
model = genai.GenerativeModel("gemini-2.0-flash")
st.title("AI Code Explainer")
prompt = st.text_area("Paste Python Code")
if st.button("Submit"):
    response = model.generate_content(
        prompt +
        " You are an AI Code Explainer specialized in Python, Java, C, C++, HTML, CSS, JavaScript, SQL, and programming concepts. Analyze the given code and explain its purpose, functionality, logic flow, variables, functions, loops, and conditions in simple language. Provide step-by-step explanations and examples when needed. If the input is not code or programming-related, respond exactly with: 'I am sorry, I can only explain programming code and coding-related concepts.'"
    )
    st.write(response.text)