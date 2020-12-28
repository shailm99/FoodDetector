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
    
    model = tf.keras.models.load_model('vgg19.h')
    
    st.write(model, size = 0.8)
    
