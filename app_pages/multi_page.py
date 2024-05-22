import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Data_visualization import visualize_data
from Powdery_mildew_detection import main as powdery_mildew_detection_main
from Summary import page5_function

class MultiPage:
    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func):
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)

        # Create a sidebar button for page navigation
        page_titles = [page['title'] for page in self.pages]
        selected_page_title = st.sidebar.radio('Menu', page_titles)

        # Find the selected page and execute its function
        selected_page = next((page for page in self.pages if page['title'] == selected_page_title), None)
        if selected_page:
            selected_page['function']()

def page1_function():
    st.write('<div class="page1-container"></div>', unsafe_allow_html=True)
    st.title("General Information")
    st.write("""
    The cherry plantation crop has the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product. Powdery Mildew is a pest that is caused by a fungus *Podosphaera clandestina*. On Leaves, 
    powdery mildew appears as patches of white, powdery or felt-like fungal growth. This can also affect the fruits of the tree. Fruit infection appears as a white powdery bloom as the fruit ripens. To check if the tree has powdery mildew, 
    it takes time and a lot of labor to check the Cherry Tree one by one in the farm.If trees have a very bad infestation, it can cause a very bad fruit production for the trees. If also uncontrolled this can cause deformities to the leaves and the fruits.
    Therefore, the company has invested in creating a Machine Learning App so that farmers can just take pictures of the leaf in trees suspected to be positive of  powdery mildew fungus.
    The aim is for an early detection and faster identification so that treatment to the plant will immediately be administered, thus ensuring a good yeild in the production.
    """, unsafe_allow_html=True)

def page2_function():
    st.title("Hypothesis and Validation")
    st.write("""
    There are distinguishable features to differentiate between a healthy cherry leaf and one with mildew. With this in mind, we hypothesize that a machine learning algorithm can accurately detect the difference between healthy leaves and mildew-infected by analyzing images.

    To validate this hypothesis, we will employ a dataset containing images of both healthy cherry leaves and leaves affected by powdery mildew. By training a machine learning model on this dataset, we aim to achieve high accuracy in classifying cherry leaves as healthy or infected.

    Additionally, we will evaluate the model's performance using various metrics such as accuracy, precision, recall, and F1 score. These metrics will provide insights into the model's ability to correctly identify mildew-infected leaves while minimizing false positives and false negatives.

    The success of our hypothesis will be determined by the model's performance on an independent test dataset, ensuring its generalization to unseen cherry leaf images.
    """)

    st.subheader("Machine Learning Model Architecture")

    st.write("""
    For our machine learning model, we will explore various deep learning architectures such as convolutional neural networks (CNNs). CNNs have shown promising results in image classification tasks due to their ability to automatically learn relevant features from raw pixel data.

    The model will be trained on a labeled dataset consisting of images of healthy cherry leaves and leaves infected with powdery mildew. We will use techniques such as data augmentation to artificially increase the size of our training dataset and improve the model's robustness.

    After training, the model will be evaluated on a separate validation dataset to assess its performance metrics. We will fine-tune the hyperparameters and optimize the model architecture based on validation results to achieve the best possible performance.

    Once the model demonstrates satisfactory performance on the validation dataset, we will deploy it to our Streamlit app for real-time inference on user-uploaded cherry leaf images.
    """)


def page3_function():
    st.title("")
    st.write(""" Can be used as a reference to see the difference between a healthy and a Powdery Milded leaf """)
    visualize_data("jupyter_notebooks/inputs/validation/healthy", "jupyter_notebooks/inputs/validation/powdery_mildew")  

def page4_function():
    st.title("")
    st.write(""" Upload the Cherry Leaf Images to see if the leaf has Powdery Mildew presence""")
    powdery_mildew_detection_main()

def main():
    # Inject custom CSS styles
    st.markdown('<link rel="stylesheet" type="text/css" href="css/styles.css">', unsafe_allow_html=True)

    # Assume 'losses' is obtained after training your model
    global losses
    history = {
        'loss': [0.1, 0.08, 0.07],
        'val_loss': [0.12, 0.11, 0.1],
        'accuracy': [0.9, 0.92, 0.93],
        'val_accuracy': [0.88, 0.89, 0.9]
    }
    losses = pd.DataFrame(history)

    my_app = MultiPage("Cherry Leaves Analysis")

    # Add pages to the app
    my_app.add_page("General Information", page1_function)
    my_app.add_page("Hypothesis", page2_function)
    my_app.add_page("Data Visualization", page3_function)
    my_app.add_page("Powdery Mildew Detection", page4_function)
    my_app.add_page("Summary", lambda: page5_function(losses))

    # Run the app
    my_app.run()

if __name__ == "__main__":
    main()
