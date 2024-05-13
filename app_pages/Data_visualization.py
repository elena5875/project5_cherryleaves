import os
import streamlit as st
from PIL import Image
import json
import matplotlib.pyplot as plt


# Function to visualize cell data
def visualize_cell_data(directory):
    # Open the JSON file
    with open('/workspace/project5_cherryleaves/jupyter_notebooks/outputs/computed_data.json', 'r') as f:
        # Load the JSON data
        data = json.load(f)

    # Print the data
    st.write("Visualized Cell Data:")
    for item in data:
        # Print each item
        st.write(item)

# Call the function to run the visualization
visualize_cell_data('/workspace/project5_cherryleaves/jupyter_notebooks/inputs/train/healthy')


# Function to load and resize images
def load_and_resize_images(directory, num_images=5, target_size=(100, 100)):
    image_files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    images = []
    for i, image_file in enumerate(image_files[:num_images]):
        image_path = os.path.join(directory, image_file)
        img = Image.open(image_path)
        img_resized = img.resize(target_size)
        images.append(img_resized)
    return images

# Function to display images in rows
def display_images_in_rows(images, num_images_per_row=5):
    num_images = len(images)
    num_rows = (num_images + num_images_per_row - 1) // num_images_per_row
    for i in range(num_rows):
        row_images = images[i * num_images_per_row: (i + 1) * num_images_per_row]
        st.image(row_images, caption=[f'Image {i+1}' for i in range(len(row_images))], width=100)

# Function to visualize cell data
def visualize_cell_data(directory):
    st.write("### Cells Visualizer")
    st.info(
        f"* The client is interested to have a study to visually differentiate "
        f"healthy leaves and leaves affected by powdery mildew.")
    
    import json

if st.checkbox("Difference between average and variability image"):
    with open("/workspace/project5_cherryleaves/jupyter_notebooks/outputs/computed_data.json", "r") as file:
        computed_data = json.load(file)
    avg_healthy = plt.imread(computed_data["avg_var_Healthy"])
    avg_powdery_mildew = plt.imread(computed_data["avg_var_Powdery_Mildew"])

    st.warning(
        f"* We notice the average and variability images didn't show "
        f"patterns where we could intuitively differentiate one to another." 
        f"However, a small difference in color pigment of the average images is seen for both labels")

    st.image(avg_healthy, caption='Healthy Leaves - Average and Variability')
    st.image(avg_powdery_mildew, caption='Powdery Mildew - Average and Variability')
    st.write("---")

if st.checkbox("Differences between average healthy and average powdery mildew leaves"):
    with open("/workspace/project5_cherryleaves/jupyter_notebooks/outputs/computed_data.json", "r") as file:
        computed_data = json.load(file)
    diff_between_avgs = plt.imread(computed_data["avg_diff"])

    st.warning(
        f"* We notice this study didn't show "
        f"patterns where we could intuitively differentiate one to another.")
    st.image(diff_between_avgs, caption='Difference between average images')

if st.checkbox("Image Montage"): 
    st.write("* To refresh the montage, click on 'Create Montage' button")
    labels = os.listdir(directory)
    label_to_display = st.selectbox(label="Select label", options=labels, index=0)

        
        # Load and display images in rows
    images = load_and_resize_images(os.path.join(directory, label_to_display))
    if images:
            display_images_in_rows(images, num_images_per_row=5)
    else:
            st.write(f"No images found in directory: {os.path.join(directory, label_to_display)}")
        
    st.write("---")

# Streamlit app
st.title('Cell Image Visualizer')

# Sidebar
st.sidebar.title('Settings')
num_images = st.sidebar.slider('Number of Images', min_value=1, max_value=10, value=5)

# Main content for healthy images
st.header('Healthy Cell Images')
healthy_images = load_and_resize_images('/workspace/project5_cherryleaves/jupyter_notebooks/inputs/train/healthy', num_images=num_images)
if healthy_images:
    st.write(f"Loaded {len(healthy_images)} healthy cell images.")
    display_images_in_rows(healthy_images)
else:
    st.write("No healthy cell images loaded.")  

# Main content for powdery mildew images
st.header('Powdery Mildew Cell Images')
powdery_mildew_images = load_and_resize_images('/workspace/project5_cherryleaves/jupyter_notebooks/inputs/train/powdery_mildew', num_images=num_images)
if powdery_mildew_images:
    st.write(f"Loaded {len(powdery_mildew_images)} powdery mildew cell images.")
    display_images_in_rows(powdery_mildew_images)
else:
    st.write("No powdery mildew cell images loaded.")

# Visualize cell data
visualize_cell_data('/workspace/project5_cherryleaves/jupyter_notebooks/inputs/train/healthy')
