import os
import streamlit as st
from PIL import Image
import json
import matplotlib.pyplot as plt
from Data_visualization import page2_function

class MultiPage:
    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func):
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page_titles = [page['title'] for page in self.pages]
        selected_page_title = st.sidebar.radio('Menu', page_titles)
        selected_page = next((page for page in self.pages if page['title'] == selected_page_title), None)
        if selected_page:
            selected_page['function']()  # Call the function corresponding to the selected page

def page1_function():
    st.title("General Information")
    # Add your content here for the General Information page

def page2_function():
    st.title("Data Visualization")
    # Add your content here for the General Information page

def page3_function():
    st.title("Powdery Mildew Detection")
    # Add your content here for the Powdery Mildew Detection page

def page4_function():
    st.title("Hypothesis and Validation")
    # Add your content here for the Hypothesis and Validation page

def page5_function():
    st.title("ML Prediction Metrics")
    # Add your content here for the ML Prediction Metrics page

def main():
    my_app = MultiPage("Cherry Leaves Analysis")

    # Add pages to the app
    my_app.add_page("General Information", page1_function)
    my_app.add_page("Data Visualization", page2_function)
    my_app.add_page("Powdery Mildew Detection", page3_function)
    my_app.add_page("Hypothesis and Validation", page4_function)
    my_app.add_page("ML Prediction Metrics", page5_function)

    # Run the app
    my_app.run()

if __name__ == "__main__":
    main()
