import streamlit as st
import os

# Set the title of the app
st.title("My Flexible HTML App")

# Load the HTML file
html_file_path = 'index.html'

# Check if the HTML file exists
if os.path.exists(html_file_path):
    # Read the HTML file
    with open(html_file_path, 'r') as file:
        html_string = file.read()
    
    # Display the HTML content in the Streamlit app
    st.components.v1.html(html_string)  # Set height to 0 for flexible height
else:
    st.error("HTML file not found. Please ensure 'index.html' is in the same directory as this script.")
