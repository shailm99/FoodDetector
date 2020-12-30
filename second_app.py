import streamlit as st
import pandas as pd 
import numpy as np

def main():
    st.title("Nutrition Facts")
    
    st.write("### Select which food(s) you would like to learn more about!")
    
    nutri_df = pd.read_csv('label_nutrients.csv', index_col = 0)
    
    
    selected = st.multiselect("Select which foods you want to learn more about!", list(nutri_df.index))
    
    
    if st.button("Submit"):
        st.balloons()
        st.write(nutri_df.loc[selected])
        
    
    
