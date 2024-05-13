import streamlit as st
from Data_visualization import visualize_data

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
    st.title("General Information")
    st.write("""
    The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product. Powdery Mildew is a pest that is caused by a fungus *Podosphaera clandestina*. On Leaves, powdery mildew appears as patches of white, powdery or felt-like fungal growth. This can also affect the fruits of the tree. Fruit infection appears as a white powdery bloom as the fruit ripens. To check if the tree has powdery mildew, it takes time and a lot of labor to check the Cherry Tree one by one in the farm.

    If trees have a very bad infestation, it can cause a very bad fruit production for the trees. If also uncontrolled this can cause deformities to the leaves and the fruits.
    """)

def page2_function():
    st.title("")
    visualize_data("/workspace/project5_cherryleaves/jupyter_notebooks/inputs/validation/healthy", "/workspace/project5_cherryleaves/jupyter_notebooks/inputs/validation/powdery_mildew")

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
