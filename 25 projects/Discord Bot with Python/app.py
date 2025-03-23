import streamlit as st
import requests

# GitHub Personal Access Token (Securely Store It, Don't Share Publicly)
TOKEN = "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"

def get_github_profile_image(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data["avatar_url"]
    else:
        return None

st.title("GitHub Profile Image Scraper")

username = st.text_input("Enter GitHub Username:")

if st.button("Get Profile Image"):
    if username:
        image_url = get_github_profile_image(username)
        if image_url:
            st.image(image_url, caption=f"GitHub Profile Image of {username}", use_column_width=True)
        else:
            st.error("User not found or API rate limit exceeded!")
    else:
        st.warning("Please enter a username!")
