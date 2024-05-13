import streamlit as st
from Data_visualization import visualize_data

def page1_function():
    st.title("General Information")
    # Add your content here for the General Information page

def page2_function():
    st.title("Data Visualization")
    visualize_data(healthy_image_dir, powdery_mildew_image_dir)

def page3_function():
    st.title("Powdery Mildew Detection")
    # Add your content here for the Powdery Mildew Detection page

def page4_function():
    st.title("Hypothesis and Validation")
    # Add your content here for the Hypothesis and Validation page

def page5_function():
    st.title("ML Prediction Metrics")
    # Add your content here for the ML Prediction Metrics page
