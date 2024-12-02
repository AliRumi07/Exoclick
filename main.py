import streamlit as st
import os

def read_html_file(file_path):
    """
    Read the contents of an HTML file and return as a string.
    
    Args:
        file_path (str): index.html
    
    Returns:
        str: Contents of the HTML file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    """
    Main Streamlit application function
    """
    st.title("HTML File Viewer")

    # Specify the path to your index.html file
    html_file_path = 'index.html'

    # Check if the file exists
    if os.path.exists(html_file_path):
        # Read the HTML file
        html_content = read_html_file(html_file_path)

        if html_content:
            # Use Streamlit's markdown to render HTML
            st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.warning(f"The file {html_file_path} does not exist in the current directory.")

if __name__ == "__main__":
    main()
