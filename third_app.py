import streamlit as st
import pandas as pd 
import numpy as np
import tensorflow as tf
import pydot
import graphviz


def main():
        
    st.title("Model Architecture")
    
    text = open('model_architecture.txt','r').read()
    
    st.write(text)
    
    
