import os
import streamlit as st
from PIL import Image

def visualize_data(healthy_image_dir, powdery_mildew_image_dir):
    st.title("Data Visualization")

    # Get the first image file in the directory for healthy leaves
    healthy_image_files = [f for f in os.listdir(healthy_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    if healthy_image_files:
        healthy_image_path = os.path.join(healthy_image_dir, healthy_image_files[0])
        healthy_image = Image.open(healthy_image_path)
        st.image(healthy_image, caption='Healthy Leaves')

        # Button to view more healthy images
        if st.button("View More Healthy Leaves"):
            display_more_images(healthy_image_dir, healthy_image_files)

    else:
        st.warning("No image files found in the directory for healthy leaves.")

    # Get the first image file in the directory for powdery mildew leaves
    powdery_mildew_image_files = [f for f in os.listdir(powdery_mildew_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    if powdery_mildew_image_files:
        powdery_mildew_image_path = os.path.join(powdery_mildew_image_dir, powdery_mildew_image_files[0])
        powdery_mildew_image = Image.open(powdery_mildew_image_path)
        st.image(powdery_mildew_image, caption='Powdery Mildew Leaves')

        # Button to view more powdery mildew images
        if st.button("View More Powdery Mildew Leaves"):
            display_more_images(powdery_mildew_image_dir, powdery_mildew_image_files)

    else:
        st.warning("No image files found in the directory for powdery mildew leaves.")

def display_more_images(directory, image_files):
    # Display additional images from the directory, 5 at a time
    st.write(f"Additional Images:")
    if "index" not in st.session_state:
        st.session_state.index = 0

    index = st.session_state.index
    for image_file in image_files[index:index+5]:
        image_path = os.path.join(directory, image_file)
        image = Image.open(image_path)
        st.image(image, caption=image_file, use_column_width=True, clamp=True, output_format='auto')

    # Button to show previous images
    if st.button("Show Previous"):
        st.session_state.index = max(0, index - 5)

    # Button to show next images
    if st.button("Show Next"):
        st.session_state.index = min(len(image_files), index + 5)

    # Button to go back to single image display
    if st.button("Go Back to Single Image"):
        st.session_state.index = 0

# Define paths to the directories containing validation images
healthy_image_dir = '/workspace/project5_cherryleaves/jupyter_notebooks/inputs/validation/healthy'
powdery_mildew_image_dir = '/workspace/project5_cherryleaves/jupyter_notebooks/inputs/validation/powdery_mildew'

# Call the visualization function with the directory paths
visualize_data(healthy_image_dir, powdery_mildew_image_dir)
