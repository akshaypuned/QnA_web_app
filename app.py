import streamlit as st
import streamlit.components.v1 as components
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import time

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    
    <style>
        .jumbotron{
            background: white;
        }

        .display-4{
            display: flex;
            justify-content: center;
            color: black;
            font-weight: bold;
        }

        p{
            display: flex;
            justify-content: center;
            font-weight: bold;
        }
    
    </style>
    
    <div class="jumbotron jumbotron-fluid">
        <div class="container" style="border:1px solid black">
            <h1 class="display-4">Q&A app</h1>
            <p class="lead">from team Analytics and AI at Mercedes Benz Consulting.</p>
        </div>
    </div>
    
    
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """,
    height=200,
)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)


def load_model():
    model_name='bert-large-uncased-whole-word-masking-finetuned-squad'
    model=pipeline('question-answering', model=model_name, tokenizer=model_name)
    return model

qa = load_model()
st.title('')
articles=st.text_area('Please enter the context')
quest= st.text_input('Ask your question')
button = st.button('Answer')
with st.spinner('Finding answer....'):
    if button and articles:
        answers = qa(question=quest, context=articles)
        st.success(answers['answer'])
