import streamlit as st

st.title("Medical LLM Project")
st.write("Welcome to the Medical LLM App!")

# Add user input for testing
user_input = st.text_area("Enter text:")
if user_input:
    st.write("You entered:", user_input)
