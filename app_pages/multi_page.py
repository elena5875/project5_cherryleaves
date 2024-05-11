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
    st.write("Page 1 Content - General Information")

def page2_function():
    st.write("Page 2 Content - Data Visualization")

def page3_function():
    st.write("Page 3 Content - Powdery Mildew Detection")

def page4_function():
    st.write("Page 4 Content - Hypothesis and Validation")

def page5_function():
    st.write("Page 5 Content - ML Prediction Metrics")

# Usage example
if __name__ == "__main__":
    my_app = MultiPage("My Streamlit App")

    # Add pages to the app
    my_app.add_page("Page 1", page1_function)
    my_app.add_page("Page 2", page2_function)
    my_app.add_page("Page 3", page3_function)
    my_app.add_page("Page 4", page4_function)
    my_app.add_page("Page 5", page5_function)

    # Run the app
    my_app.run()
