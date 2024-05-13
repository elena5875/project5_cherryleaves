import os
import streamlit as st
from PIL import Image
import itertools
import random
import matplotlib.pyplot as plt




def visualize_data(healthy_image_dir, powdery_mildew_image_dir):
    st.title("Data Visualization")

    # Get image files from directories
    healthy_image_files = [f for f in os.listdir(healthy_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    powdery_mildew_image_files = [f for f in os.listdir(powdery_mildew_image_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

    # Display healthy leaves
    display_images(healthy_image_dir, healthy_image_files[:5], "Healthy")

    # Display powdery mildew leaves
    display_images(powdery_mildew_image_dir, powdery_mildew_image_files[:5], "Powdery Mildew")


def display_images(directory, image_files, label):
    st.write(f"Images from {os.path.basename(directory)}:")

    if not image_files:
        st.warning(f"No image files found in the directory for {label}.")
        return

    # Initialize index for image selection
    if f"index_{label.lower().replace(' ', '_')}" not in st.session_state:
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = 0

    # Display selected images with adjustable width
    selected_image_index = st.session_state[f"index_{label.lower().replace(' ', '_')}"]
    col1, col2 = st.beta_columns(2)

    # Show first image
    selected_image_path1 = os.path.join(directory, image_files[selected_image_index])
    selected_image1 = Image.open(selected_image_path1)
    image_width = st.selectbox(f"Choose Image Width for {label} (pixels):", options=[100, 200, 300], index=0, key=f"selectbox_{label.lower().replace(' ', '_')}")
    col1.image(selected_image1, caption=f"{label} Image {selected_image_index+1}", width=image_width, use_column_width=True)

    # Show second image
    selected_image_index2 = selected_image_index + 1 if selected_image_index + 1 < len(image_files) else 0
    selected_image_path2 = os.path.join(directory, image_files[selected_image_index2])
    selected_image2 = Image.open(selected_image_path2)
    col2.image(selected_image2, caption=f"{label} Image {selected_image_index2+1}", width=image_width, use_column_width=True)

    # Show Next and Show Previous buttons
    col1, col2, col3 = st.beta_columns([1, 2, 1])
    if col2.button("Show Previous", key=f"prev_button_{label.lower().replace(' ', '_')}"):
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = max(0, selected_image_index - 1)
    if col2.button("Show Next", key=f"next_button_{label.lower().replace(' ', '_')}"):
        st.session_state[f"index_{label.lower().replace(' ', '_')}"] = (selected_image_index + 1) % len(image_files)


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path+'/'+ label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = Image.open(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.size
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[0]}px x Height {img_shape[1]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}") 



