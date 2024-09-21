import streamlit as st
from scrape import scrape_website

st.title("AI web scraper")

url = st.text_input("Enter a Website URL: ")

if st.button("Scrape site"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    print(result)