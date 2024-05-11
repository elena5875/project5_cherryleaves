import os
import streamlit as st

def data_visualization():
    st.title("Data Visualization")
    st.write("Business Requirement 1: Visual differentiation of healthy cherry leaves and powdery mildew leaves")
    
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

        # Create output directory for the label if it doesn't exist
        output_label_dir = os.path.join(output_dir, label)
        os.makedirs(output_label_dir, exist_ok=True)

        # Plot the images
        num_images = min(len(image_files), 5)  # Limit to maximum 5 images for visualization
        st.subheader(f'Images of {label} (Sample)')

        # Save and display the images
        for i in range(num_images):
            image_filename = f'image_{i+1}.jpg'  # Save as JPEG
            image_path = os.path.join(directory, image_files[i])
            st.image(image_path, caption=f'Image {i+1}')

            # Save the image
            output_image_path = os.path.join(output_label_dir, image_filename)
            st.markdown(f"![{image_filename}]({output_image_path})")

    # Visualize and save images in the 'healthy' directory
    visualize_images(healthy_dir, 'Healthy')

    # Visualize and save images in the 'powdery_mildew' directory
    visualize_images(powdery_mildew_dir, 'Powdery Mildew')

# Call the function to run the visualization
data_visualization()
