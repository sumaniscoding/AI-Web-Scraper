import streamlit as st

st.title("AI web scraper")

url = st.text_input("Enter a Website URL: ")

if st.button("Scrape site"):
    st.write("Scraping the website...")