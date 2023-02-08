## Libraries to be used --------------------------
import streamlit as st
from transformers import pipeline
## for WordPress sender
import json
import requests
from urllib.parse import urljoin
from datetime import datetime

## Page title and favicon ------------------------
st.set_page_config(page_title = "Article Generator with a Sentence",
                   page_icon = "https://em-content.zobj.net/source/skype/289/robot_1f916.png")

## Page content logo and header ------------------
st.text("")
st.image("https://em-content.zobj.net/source/skype/289/robot_1f916.png", width=125,)


## Title -----------------------------------------
st.title("Article Generator with a Sentence")

## Header/Subheader ------------------------------
## st.header("This is header")
st.subheader("Generate an article with just one sentence.")

## Text input
starting_sentence = st.text_input("Type here a starting sentence 👇", "Type here...")


## Buttons ---------------------------------------
if st.button("Submit"):

    # Using GPT-NEO (model size min 125M ~ max 2.7B)
    # gen = pipeline('text-generation', model ='EleutherAI/gpt-neo-2.7B')
    # gen = pipeline('text-generation', model ='EleutherAI/gpt-neo-1.3B')
    gen = pipeline('text-generation', model ='EleutherAI/gpt-neo-125M')

    # context = "Deep Learning is a sub-field of Artificial Intelligence."
    context = starting_sentence

    output = gen(context,
                 max_length=600,
                 do_sample=True,
                 temperature=0.9,
                 pad_token_id=50256,
                 num_return_sequences=1)

    # placeholder = st.text(output)
    txt = st.text_area("Ta-da~! Here comes the article. You can edit it directly if you want. ",
                       output[0]['generated_text'],
                       height=1000)
