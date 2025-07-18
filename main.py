import streamlit as st
import base64
# Addign a title to my webapp
st.title("DATANAUT")
from scrape import scrape_it, split_dom_content, extract_main_content, clean_the_body_content

from bs4 import BeautifulSoup
# Set page config
st.set_page_config(page_title="My App with Background", layout="wide")

# Convert the local image to Base64 and embed it into CSS
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpg;base64,{encoded}");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Use your local image here
add_bg_from_local("ast.jpg")


#Here we will make users to enter the url they want to scrap in 
url = st.text_input("Enter the Website URL: ")

if(st.button("Scrape it UP")):
  st.write("Gathering information via DATANAUT.... ")
  result = scrape_it(url) # this function form scape.py lib will scrape the website with that particular url

  body_content = extract_main_content(result)
  cleaned_content = clean_the_body_content(body_content)

  st.session_state.dom_content = cleaned_content

  with st.expander("View DOM Content"):
     st.text_area("DOM Content", cleaned_content, height = 300)

  # now we will pass the dom content by user as a prompt to llm to retrive the data 


if "dom_content" in st.session_state:
   parse_description = st.text_area("Ask for the data, you want to get from DATANAUT")
   if st.button("Parse it"):
      if parse_description:
         st.write("Parsing the Content....")

         dom_chunks = split_dom_content(st.session_state.dom_content)