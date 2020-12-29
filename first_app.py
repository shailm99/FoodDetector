import streamlit as st
import numpy as np 
import pandas as pd 
import tensorflow as tf
from PIL import Image
import os
import io
import zipfile
import wget
import tempfile


def main():


    temp_dir = tempfile.TemporaryDirectory()
    paths = temp_dir.name
    
    url = 'https://vgg19-fooddetector.s3-ap-southeast-1.amazonaws.com/vgg19.h.zip'
    wget.download(url, os.path.join(paths,'vgg19.h.zip'))
    with zipfile.ZipFile(os.path.join(paths,'vgg19.h.zip'), 'r') as zip_ref:
        zip_ref.extractall(paths)
    
    model = tf.keras.models.load_model(os.path.join(paths,'vgg19.h'))
    
    # use temp_dir, and when done:
    temp_dir.cleanup()


    st.title("FoodDetector")
    
    st.write("## You eat, we detect.")
    
    st.write("#### Add a picture of what you're eating at the moment, and we will tell you what it is")
    
    image = None
    
    gender = st.selectbox('Your Gender/Sex', ['Male', 'Female', 'Gender Diverse'])
    age = st.slider('Age', 0, 110, 20)
    weight = st.slider("Current Weight In Pounds", 0, 300, 150)
    height = st.slider("Current Height in Cm", 0, 250, 140)
    activity = st.selectbox("Your Activity Level", ["High", "Medium", "Low"])
    
    multipler = {"High" : 2.25, "Medium" : 1.76, "Low" : 1.53}
    
    act_multipler = multipler[activity]
    
    
    # Using Harris–Benedict BMR calculate calories needed
    if gender == "Male":
        calories_needed = act_multipler * (5  + (4.5 * weight) + (6.25 * height) - (5 * age))
    elif gender == "Female":
        calories_needed = act_multipler * (-161  + (4.5 * weight) + (6.25 * height) - (5 * age))
    else:
        calories_needed = act_multipler * (-75  + (4.5 * weight) + (6.25 * height) - (5 * age))
    
    
    image = st.file_uploader("The image of your meal!", ["png", "jpg", "jpeg", 'HEIC'], key = 'file')
    
    
    
    labels = open('labels.txt')
    classes = labels.read()
    classes = classes.split(sep = '\n')
    classes = classes[:-1]
    labels.close()
    
    nutri_df = pd.read_csv('label_nutrients.csv', index_col = 0)
    
    
    def make_prediction(img, model = model):
       img = img.convert('RGB')
       img = img.resize((224,224), Image.NEAREST)
       img = tf.keras.preprocessing.image.img_to_array(img)
       img_array = tf.expand_dims(img, 0) 
       prediction = model.predict(img_array) 
       pred_class = np.argmax(prediction) 
       return classes[pred_class]
    
    if image is not None:
        col1, col2 = st.beta_columns(2)
        st.balloons()
        with col1:
            image_to_share = Image.open(image)
            st.image(image_to_share, width=265)
        with col2:
            st.write("## The Predicted Class Is:")
            predicted_class = make_prediction(image_to_share)
            st.write('# {}'.format(predicted_class))
            sub_df = nutri_df.loc[predicted_class].T
            st.write(sub_df)
            calories_remaining = calories_needed - sub_df.iloc[0]
            st.write("Using the Harris–Benedict BMR Equation based upon your gender, age, weight, height, and activity level")
            st.write("#### You will have {} calories remaining".format(round(calories_remaining)))
            
        

            
    
    
    
    
    
