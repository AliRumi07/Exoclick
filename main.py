import streamlit as st
import streamlit.components.v1 as components

# Set page title
st.set_page_config(page_title="My Streamlit App")

def main():
    # Read the HTML file
    with open('templates/index.html', 'r') as file:
        html_content = file.read()
    
    # Render the HTML
    components.html(html_content, height=600)

if __name__ == '__main__':
    main()
