import streamlit as st


def main():
        
    st.title("Model Architecture")
    
    text = open('model_architecture.txt','r').read()
    
    st.write(text)
    
    
