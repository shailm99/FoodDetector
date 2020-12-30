# FoodDetector

Check out the actual application [here](https://food-detect0r.herokuapp.com/)

Check out a video demo of the application [here](https://drive.google.com/file/d/1T-gDyYSAYeYRr_mWbKw0weFCymS77uea/view?usp=sharing)

## Overview 

FoodDetector is a one stop shop for food transparency. The main feature of this application is the use of deep learning, in particular a convolutional neural network, to detect what food a person is currently eating based upon a photo of their dish. Essentially, the application takes in a user inputted image, feeds it into the convolutional neural network, and outputs the predicted class of the image. Besides this, the application relays the key nutrient breakdown of the predicted food class to the user, and allows them to learn more about what they are eating. In this application, the user is also able to customize their age, weight, height, activity, and gender in order to get customized calories-remaining recommendations based upon the Harris–Benedict BMR formula.

## References

[The Food Dataset](https://s3.amazonaws.com/fast-ai-imageclas/food-101.tgz)

[Streamlit Documentation](https://docs.streamlit.io/en/stable/index.html)

[Tensorflow Documentation](https://www.tensorflow.org/api_docs)

[NutrienTrackeR](https://cran.r-project.org/web/packages/NutrienTrackeR/index.html)
