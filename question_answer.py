import requests
import streamlit as st
from transformers import pipeline

st.header("MICA: Your regulatory compliance assistant")
url = st.text_input("Enter a url")
question = st.text_input("Ask me a question")
if st.button("Go"):
    nlp = pipeline("question-answering")
    response = requests.get(url, verify=False)
    data = response.content
    model_answer = nlp({"question": question, "context": str(data)})
    score = float(model_answer["score"]) * 100
    st.text_input("Answer", value=model_answer["answer"])
    st.text_area("How confident am I about this answer?", value=f"{score:.2f}%")
