import streamlit as st


def main():
    
    st.title("About this project")
    
    text = open('project_description.txt','r').read()
    
    st.write(text)
    
