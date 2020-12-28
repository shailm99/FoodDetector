import streamlit as st
import pandas as pd 
import numpy as np

def main():
    
    st.title("About this project")
    
    text = open('project_description.txt','r').read()
    
    st.write(text)
    
