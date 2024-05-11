import streamlit as st

# Class to generate multiple Streamlit pages using an object-oriented approach 
class MultiPage: 

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️") 
    
    def add_page(self, title, func) -> None: 
        self.pages.append({"title": title, "function": func })

    def run(self):
        st.title(self.app_name)
        page_titles = [page['title'] for page in self.pages]
        selected_page_title = st.sidebar.radio('Menu', page_titles)
        selected_page = next((page for page in self.pages if page['title'] == selected_page_title), None)
        if selected_page:
            selected_page['function']()  # Call the function corresponding to the selected page

# Define functions for each page
def page1_function():
    st.title("General Information")
    st.subheader("Quick Page Summary")
    st.write("""
    The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.
    
    Powdery Mildew is a pest that is caused by a fungus Podosphaera clandestina. On Leaves, powdery mildew appears as patches of white, powdery or felt-like fungal growth. This can also affect the fruits of the tree. Fruit infection appears as a white powdery bloom as the fruit ripens.
    
    To check if the tree has powdery mildew, it takes time and a lot of labor to check the Cherry Tree one by one in the farm.
    
    If trees have a very bad infestation, it can cause a very bad fruit production for the trees. If also uncontrolled this can cause deformities to the leaves and the fruits.
    """)

def page2_function():
    st.title("Data Visualization")
    # Add your visualization content here

def page3_function():
    st.title("Powdery Mildew Detection")
    # Add your powdery mildew detection content here

def page4_function():
    st.title("Hypothesis and Validation")
    # Add your hypothesis and validation content here

def page5_function():
    st.title("ML Prediction Metrics")
    # Add your ML prediction metrics content here

# Usage example
if __name__ == "__main__":
    my_app = MultiPage("")

    # Add pages to the app
    my_app.add_page("Page 1", page1_function)
    my_app.add_page("Page 2", page2_function)
    my_app.add_page("Page 3", page3_function)
    my_app.add_page("Page 4", page4_function)
    my_app.add_page("Page 5", page5_function)

    # Run the app
    my_app.run()
