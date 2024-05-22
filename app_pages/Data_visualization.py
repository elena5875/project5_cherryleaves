import os
import streamlit as st
from PIL import Image
import numpy as np
import itertools
import random
import matplotlib.pyplot as plt
import seaborn as sns

def is_leaf(image_array, aspect_ratio_threshold=0.8, green_pixel_threshold=0.2):
    aspect_ratio = image_array.shape[0] / image_array.shape[1]
    if aspect_ratio < aspect_ratio_threshold:
        print("Image aspect ratio suggests it's not a leaf.")
        return False
    
    green_pixels = np.mean(image_array[:, :, 1] / 255)
    if green_pixels < green_pixel_threshold:
        print("Not enough green pixels. Image may not be a leaf.")
        return False
    
    return True

def visualize_data(healthy_image_dir, powdery_mildew_image_dir):
    st.title("Cherry Leaf Disease Detection")

    st.header("Download Cherry Leaf Images for Live Prediction")
    st.markdown("""
    You can download a set of cherry leaf images for live prediction from the Kaggle dataset: 
    [Download Cherry Leaf Images](https://www.kaggle.com/codeinstitute/cherry-leaves/download)
    """)

    healthy_image_files = [f for f in os.listdir(healthy_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    powdery_mildew_image_files = [f for f in os.listdir(powdery_mildew_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

    display_images(healthy_image_dir, healthy_image_files[:5], "Healthy")
    display_images(powdery_mildew_image_dir, powdery_mildew_image_files[:5], "Powdery Mildew")

def display_images(directory, image_files, label):
    st.write(f"Images from {os.path.basename(directory)}:")

    if not image_files:
        st.warning(f"No image files found in the directory for {label}.")
        return

    if f"index_{label.lower().replace(' ', '_')}" not in st.session_state:
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = 0

    selected_image_index = st.session_state[f"index_{label.lower().replace(' ', '_')}"]
    cols = st.columns(2)

    selected_image_path1 = os.path.join(directory, image_files[selected_image_index])
    selected_image1 = Image.open(selected_image_path1)
    image_width = st.selectbox(f"Choose Image Width for {label} (pixels):", options=[100, 200, 300], index=0, key=f"selectbox_{label.lower().replace(' ', '_')}")
    cols[0].image(selected_image1, caption=f"{label} Image {selected_image_index+1}", width=image_width, use_column_width=True)

    selected_image_index2 = selected_image_index + 1 if selected_image_index + 1 < len(image_files) else 0
    selected_image_path2 = os.path.join(directory, image_files[selected_image_index2])
    selected_image2 = Image.open(selected_image_path2)
    cols[1].image(selected_image2, caption=f"{label} Image {selected_image_index2+1}", width=image_width, use_column_width=True)

    prev_button = cols[0].button("Show Previous", key=f"prev_button_{label.lower().replace(' ', '_')}")
    next_button = cols[1].button("Show Next", key=f"next_button_{label.lower().replace(' ', '_')}")

    if prev_button:
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = max(0, selected_image_index - 1)
    elif next_button:
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = (selected_image_index + 1) % len(image_files)

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(os.path.join(dir_path, label_to_display))
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            st.warning(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        plot_idx = list(itertools.product(range(nrows), range(ncols)))

        fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
        for idx, (i, j) in enumerate(plot_idx):
            img_path = os.path.join(dir_path, label_to_display, img_idx[idx])
            img = Image.open(img_path)
            axes[i, j].imshow(img)
            axes[i, j].axis('off')
        st.pyplot(fig)
