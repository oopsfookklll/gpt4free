import streamlit as st
from g4f.Provider.Providers import Bing, Phind

def main():
    st.title("Question Answering with Bing and Phind")

    question = st.text_input("Enter your question:")
    text_attachment = st.file_uploader("Upload a text attachment:")

    if st.button("Get Answer"):
        if 'gpt-4' in Bing.model:
            bing_answer = Bing._create_completion('gpt-4', [{'role': 'user', 'content': question}], True)
            st.write("Answer from Bing:")
            st.write(next(bing_answer))
        else:
            st.write("Bing does not support the 'gpt-4' model.")
    
        if 'gpt-4' in Phind.model:
            phind_answer = Phind._create_completion('gpt-4', [{'role': 'user', 'content': question}], True)
            st.write("Answer from Phind:")
            st.write(next(phind_answer))
        else:
            st.write("Phind does not support the 'gpt-4' model.")

if __name__ == "__main__":
    main()