import os
import streamlit as st
import utils.text_processing  # Import your module

st.title("WHATSAPP CHAT ANALYZER")

uploaded_file = st.file_uploader("Choose a .txt file to upload", type=["txt"])



if uploaded_file is not None:
    # Save the file to a directory
    file_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(uploaded_file.getvalue().decode("utf-8", errors="replace"))

    # Pass the file path to your function
    df = utils.text_processing.preprocess_text(file_path)

    # Display DataFrame (Optional)
    st.write(df)
