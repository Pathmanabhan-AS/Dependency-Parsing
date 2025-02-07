import streamlit as st 
import pandas as pd 
from parser import parse_sentence 
 
st.set_page_config(page_title="Dependency Parsing App", layout="wide") 
 
st.title("Dependency Parsing Web App ") 
st.write("Analyze the dependency structure of a sentence using **Stanza**.") 
 
sentence = st.text_area("Enter a sentence:", "The quick brown fox jumps over the lazy dog.") 
 
if st.button("Parse Sentence"): 
    if sentence.strip(): 
        df = parse_sentence(sentence) 
        st.write("### Dependency Parsing Result") 
        st.dataframe(df) 
        st.write("### Parsed Sentence Tree:") 
        for _, row in df.iterrows(): 
            st.write(f"**{row['Token']}** → {row['Head']} ({row['Relation']})") 
    else: 
        st.warning("Please enter a valid sentence.") 
 
st.markdown("---") 
st.markdown("NLP Project ") 