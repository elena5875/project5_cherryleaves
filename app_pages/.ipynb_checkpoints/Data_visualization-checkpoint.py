import os
import streamlit as st

import pandas as pd
import numpy as np
import seaborn as snscd
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def data_visualization():
    st.title("Data Visualization")
    st.write("The visual example of a Healthy Cherry Leaves and A Cherry Leaves with Powdery Mildew present")
    
    # Paths to the directories containing images
    healthy_dir = '/workspace/project5_cherryleaves/jupyter_notebooks/inputs/train/healthy'
    powdery_mildew_dir = '/workspace/project5_cherryleaves/jupyter_notebooks/inputs/train/powdery_mildew'

    # Output directory
    output_dir = '/workspace/project5_cherryleaves/jupyter_notebooks/outputs/train'

    # Function to visualize images in a directory and save them
    def visualize_images(directory, label):
        # Get list of image files in the directory
        image_files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

        # Check if there are any images in the directory
        if not image_files:
            st.write(f"No images found in directory: {directory}")
            return

        # Plot the images
        num_images = min(len(image_files), 5)  
        st.subheader(f'Images of {label} (Sample)')

        # Display images in a row
        cols = st.beta_columns(num_images)
        for i, col in enumerate(cols):
            image_path = os.path.join(directory, image_files[i])
            col.image(image_path, caption=f'Image {i+1}')

    # Visualize and save images in the 'healthy' directory
    visualize_images(healthy_dir, 'Healthy')

    # Visualize and save images in the 'powdery_mildew' directory
    visualize_images(powdery_mildew_dir, 'Powdery Mildew')

def page_cells_visualizer_body():
    st.write("### Cells Visualizer")
    st.info(
        f"* The client is interested to have a study to visually differentiate "
        f"an parasitized and uninfected cell.")
    
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
        avg_powdery_mildew = plt.imread("/workspace/project5_cherryleaves/jupyter_notebooks/outputs/train/powdery_mildew")
        avg_healthy = plt.imread("/workspace/project5_cherryleaves/jupyter_notebooks/outputs/train/healthy")

        st.image(avg_powdery_mildew, caption='Powdery Mildew Cell - Average and Variability')
        st.image(avg_healthy, caption='Healthy Cell - Average and Variability')


        st.warning(
            f"* We notice the average and variability images didn't show "
            f"patterns where we could intuitively differentiate one to another." 
            f"However, a small difference in color pigment of the average images is seen for both labels")

        st.image(avg_parasitized, caption='Parasitized Cell - Average and Variability')
        st.image(avg_uninfected, caption='Uninfected Cell - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average parasitized and average uninfected cells"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"* We notice this study didn't show "
            f"patterns where we could intuitively differentiate one to another.")
        st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
        st.write("* To refresh the montage, click on 'Create Montage' button")
        my_data_dir = 'inputs/malaria_dataset/cell_images'
        labels = os.listdir(my_data_dir+ '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):      
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10,25))
        st.write("---")

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    # Get list of image files in the directory
        image_files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

        # Check if there are any images in the directory
        if not image_files:
            st.write(f"No images found in directory: {directory}")
            return

        # Plot the images
        num_images = min(len(image_files), 5)  
        st.subheader(f'Images of {label} (Sample)')

        # Display images in a row
        cols = st.beta_columns(num_images)
        for i, col in enumerate(cols):
            image_path = os.path.join(directory, image_files[i])
            col.image(image_path, caption=f'Image {i+1}')

            # Visualize and save images in the 'healthy' directory
            visualize_images(healthy_dir, 'Healthy')

            # Visualize and save images in the 'powdery_mildew' directory
            visualize_images(powdery_mildew_dir, 'Powdery Mildew')


# Call the function to run the visualization
data_visualization()
page_cells_visualizer_body()
