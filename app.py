import streamlit as st
import streamlit.components.v1 as components
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import time

components.html(
    """
    <html>
        <head>
            <script type="text/javascript" src="https://hosted.us.uneeq.io/deploy/8c831401-32df-4fa8-8744-1e67df4d5289"></script>
        </head>
        
    </html>
            """,
            height=500,
            width=740,
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
