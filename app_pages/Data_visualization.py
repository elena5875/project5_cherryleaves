import os
import streamlit as st
from PIL import Image


def visualize_data(healthy_image_dir, powdery_mildew_image_dir):
    st.title("Data Visualization")

    # Get image files from directories
    healthy_image_files = [f for f in os.listdir(healthy_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    powdery_mildew_image_files = [f for f in os.listdir(powdery_mildew_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

    # Display healthy leaves
    display_images(healthy_image_dir, healthy_image_files, "Healthy")

    # Display powdery mildew leaves
    display_images(powdery_mildew_image_dir, powdery_mildew_image_files, "Powdery Mildew")

def display_images(directory, image_files, label):
    st.write(f"Images from {os.path.basename(directory)}:")

    if not image_files:
        st.warning(f"No image files found in the directory for {label}.")
        return

    # Initialize index for image selection
    if f"index_{label.lower().replace(' ', '_')}" not in st.session_state:
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = 0

    # Display selected image with adjustable width
    selected_image_path = os.path.join(directory, image_files[st.session_state[f"index_{label.lower().replace(' ', '_')}"]])
    selected_image = Image.open(selected_image_path)
    image_width = st.selectbox(f"Choose Image Width for {label} (pixels):", options=[100, 200, 300], index=1, key=f"selectbox_{label.lower().replace(' ', '_')}")
    st.image(selected_image, width=image_width)

    # Show Next and Show Previous buttons
    col1, col2, col3 = st.beta_columns([1, 2, 1])
    if col2.button("Show Previous", key=f"prev_button_{label.lower().replace(' ', '_')}"):
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = max(0, st.session_state[f"index_{label.lower().replace(' ', '_')}"] - 1)
    if col2.button("Show Next", key=f"next_button_{label.lower().replace(' ', '_')}"):
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = min(len(image_files) - 1, st.session_state[f"index_{label.lower().replace(' ', '_')}"] + 1)

# Define paths to the directories containing validation images
healthy_image_dir = '/workspace/project5_cherryleaves/jupyter_notebooks/inputs/validation/healthy'
powdery_mildew_image_dir = '/workspace/project5_cherryleaves/jupyter_notebooks/inputs/validation/powdery_mildew'

# Call the visualization function with the directory paths
visualize_data(healthy_image_dir, powdery_mildew_image_dir)

