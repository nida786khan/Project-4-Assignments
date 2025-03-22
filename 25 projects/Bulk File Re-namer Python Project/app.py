# Bulk File Renamer
import os
import streamlit as st

def rename_files(folder_path, prefix):
    try:
        files = os.listdir(folder_path)
        for index, file in enumerate(files):
            file_ext = os.path.splitext(file)[1]
            new_name = f"{prefix}_{index}{file_ext}"
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
        return "Files renamed successfully!"
    except Exception as e:
        return f"Error: {e}"

st.title("Bulk File Renamer")
folder = st.text_input("Enter folder path")
prefix = st.text_input("Enter prefix for new filenames")

if st.button("Rename Files"):
    if folder and prefix:
        result = rename_files(folder, prefix)
        st.write(result)
    else:
        st.write("Please enter both folder path and prefix.")
