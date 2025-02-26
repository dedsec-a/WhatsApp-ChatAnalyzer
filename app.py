import streamlit as st
import os
import utils.text_processing
import utils.data_visualization
import utils.sentiment_analysis

# App Title
st.title("WhatsApp Chat Analyzer 📊")

# File Upload Section
uploaded_file = st.file_uploader("Upload WhatsApp Chat (.txt)", type=["txt"])


if uploaded_file is not None:
    # Save the uploaded file
    chat_data = uploaded_file.getvalue().decode("utf-8")
    file_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded successfully: {uploaded_file.name}")

    # Read File Content (Optional Preview)
    with open(file_path, "r", encoding="utf-8") as file:
        chat_data = file.read()
        st.text_area("File Preview:", chat_data[:1000], height=300)  # Show first 1000 chars

    # Placeholder for Text Preprocessing
    if st.button("Process Chat Data"):
        st.info("🔄 Processing chat data...")
        df = utils.text_processing.load_text_data(chat_data)
        utils.data_visualization.activity_trend(df=df,frequency="M")
        utils.data_visualization.activity_trend(df=df,frequency="W")
        utils.data_visualization.activeUsers(df=df , frequency="M")
        utils.data_visualization.activeUsers(df=df,frequency="W")
        utils.data_visualization.create_wordcloud(df=df)
        

        



        




   


