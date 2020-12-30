import first_app, second_app, third_app, fourth_app
import streamlit as st


Pages = {"Detect My Food": first_app, "Nutrition Facts": second_app,
    "Model Architecture": third_app, "About the Project": fourth_app
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(Pages.keys()))

Pages[selection].main()
