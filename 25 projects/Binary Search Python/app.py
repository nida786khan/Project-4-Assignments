import streamlit as st
import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Streamlit UI
st.title("🔍 Binary Search Algorithm")

size = st.slider("Select list size:", 5, 20, 10)
arr = sorted(random.sample(range(1, 100), size))
st.write("### 🔢 Sorted List:", arr)

target = st.number_input("Enter a number to search:", min_value=1, max_value=100, step=1)

if st.button("Search"):
    result = binary_search(arr, target)
    if result != -1:
        st.success(f"🎯 Element {target} found at index {result}")
    else:
        st.error(f"❌ Element {target} not found in the list")
