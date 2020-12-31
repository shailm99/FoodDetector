import streamlit as st
import numpy as np 
import pandas as pd 
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import os
import io



def main():

    st.title("FoodDetector")
    
    st.write("## You eat, we detect.")
    
    st.write("#### Add a picture of what you're eating at the moment, and we will tell you what it is")
    
    image = None # intialize a variable to store the image
    
    # Ask the user for their information so we can generate their calories required
    gender = st.selectbox('Your Gender/Sex', ['Male', 'Female', 'Gender Diverse'])
    age = st.slider('Age', 0, 110, 20)
    weight = st.slider("Current Weight In Pounds", 0, 300, 150)
    height = st.slider("Current Height in Cm", 0, 250, 140)
    activity = st.selectbox("Your Activity Level", ["High", "Medium", "Low"])
    
    multipler = {"High" : 2.25, "Medium" : 1.76, "Low" : 1.53} # The Basal multipler based upon the activity level(Harris–Benedict BMR)
    
    act_multipler = multipler[activity]
    
    
    # Using Harris–Benedict BMR calculate calories needed
    if gender == "Male":
        calories_needed = act_multipler * (5  + (4.5 * weight) + (6.25 * height) - (5 * age))
    elif gender == "Female":
        calories_needed = act_multipler * (-161  + (4.5 * weight) + (6.25 * height) - (5 * age))
    else:
        calories_needed = act_multipler * (-75  + (4.5 * weight) + (6.25 * height) - (5 * age))
    
    
    # Allow the user to upload a image of their meal
    image = st.file_uploader("The image of your meal!", ["png", "jpg", "jpeg", 'HEIC'], key = 'file')
    
    
    # Load and Compile the Model
    model = load_model('vgg19.h', compile = False)
    loss = 'sparse_categorical_crossentropy'
    optimizer = 'adam'
    model.compile(loss = loss, optimizer = optimizer)
    
    # Open the labels.text, which stores the class names 
    labels = open('labels.txt')
    classes = labels.read()
    classes = classes.split(sep = '\n')
    classes = classes[:-1]
    labels.close()
    
    # read the nutritional facts dataframe
    nutri_df = pd.read_csv('label_nutrients.csv', index_col = 0)
    
    
    def make_prediction(img, model = model):
       '''
        This function takes in a image and model, and uses the model to predict the class of the image 
       '''
       img = img.convert('RGB')
       img = img.resize((224,224), Image.NEAREST)
       img = tf.keras.preprocessing.image.img_to_array(img)
       img_array = tf.expand_dims(img, 0) 
       prediction = model.predict(img_array) 
       pred_class = np.argmax(prediction) 
       return classes[pred_class]
   

    if image is not None: # if the image is an actual file then
        col1, col2 = st.beta_columns(2) # split our layout into two columns
        st.balloons() # display the ballons
        with col1: # the first column in our layout will display the image
            image_to_share = Image.open(image)
            st.image(image_to_share, width=265)
        with col2: # the second column will display the predicted class, nutritional facts and reccomended calories remaining
            st.write("## The Predicted Class Is:")
            predicted_class = make_prediction(image_to_share)
            st.write('# {}'.format(predicted_class))
            sub_df = nutri_df.loc[predicted_class].T
            st.write(sub_df)
            calories_remaining = calories_needed - sub_df.iloc[0]
            st.write("Using the Harris–Benedict BMR Equation based upon your gender, age, weight, height, and activity level")
            st.write("#### You will have {} calories remaining".format(round(calories_remaining)))
            image = None
            
        

            
    
    
    
    
    
