import requests
import streamlit as st
from transformers import pipeline

from simpletransformers.question_answering import QuestionAnsweringModel

model = QuestionAnsweringModel('bert', 'bert-base-cased', args=train_args)

st.header("MICA: Your regulatory compliance assistant")
#url = st.text_input("Enter a url")
data = st.text_input("Enter text")
question = st.text_input("Ask me a question")
question_2 = st.text_input("Ask me another question")
if st.button("Go"):
    nlp = pipeline("question-answering")
    #response = requests.get(url, verify=False)
    data = response.content
    model_answers = nlp({"question": [question, question_2], "context": str(data)})
    for model_answer in model_answers:
        score = float(model_answer["score"]) * 100
        st.text_input("Answer", value=model_answer["answer"])
        st.text_area("How confident am I about this answer?", value=f"{score:.2f}%")
