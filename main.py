import streamlit as st

def read_html_file(file_path):
    """
    Read the contents of an HTML file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "<h1>HTML File Not Found</h1>"

def main():
    """
    Streamlit app to display the HTML page
    """
    # Set page configuration
    st.set_page_config(
        page_title="Blog Posts",
        page_icon=":memo:",
        layout="wide"
    )

    # Hide Streamlit default styling
    st.markdown("""
    <style>
    .reportview-container {
        margin-top: -2em;
    }
    .stDeployButton {
        display: none;
    }
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

    # Read the HTML file
    html_content = read_html_file('index.html')

    # Display the HTML content
    st.components.v1.html(html_content, scrolling=True, height=1200)

    # Optional: Add some Streamlit-specific interactions
    st.sidebar.header("Blog Post Controls")
    filter_option = st.sidebar.selectbox(
        "Filter Posts",
        ["All Posts", "Technology", "Design", "Development"]
    )

    # You can add more interactive elements here if needed

if __name__ == "__main__":
    main()
