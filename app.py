import streamlit as st
import openai

# Azure OpenAI setup
openai.api_type = "azure"
openai.api_base = "https://hospai.openai.azure.com/openai/deployments/gpt-4-deployment/chat/completions?api-version=2024-08-01-preview"
openai.api_version = "2024-08-01-preview"
openai.api_key = st.secrets["openai"]["api_key"]


deployment_name = "gpt-4-deployment"

st.title("Medical LLM Chatbot")
st.write("Ask me anything about medical topics!")

# User input
user_input = st.text_area("Enter your medical question:")

if st.button("Get Answer"):
    if user_input:
        try:
            # OpenAI API Call
            response = openai.ChatCompletion.create(
                engine=deployment_name,
                messages=[{"role": "user", "content": user_input}],
                max_tokens=500
            )
            answer = response["choices"][0]["message"]["content"]
            st.write("### 🤖 AI Response:")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
