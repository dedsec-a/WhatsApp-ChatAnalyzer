import os ,sys

folders = [
    "utils",
    "models",
    "data",
    "reports",
    "notebook",
    "assets",
    "config"
    "templates"
]


files = {
    "app.py" : "",
    "requirements.txt" : "",
    "utils/__init__.py" : "",
    "utils/text_processing.py" : "#PlaceHolder for Pre-processing Functions",
    "utils/sentiment_analysis.py" : "# Placeholder for Sentiment Analysis Logic",
    "utils/pdf_generator.py" : "# Place Holder for Pdf Generation Logic",
    "utils/data_visualization.py" : "# Placeholder for Data Visulasation Functions",
    "models/.gitkeep" : "" ,# To Keep the Track of the Empty Folder
    "data/Sample_Chat.txt" : "The Raw Data will go here",
    "Notebook/Expriments.ipynb" : "# jupyter Notebook for Exprementing",
    "templates/index.html" : "# The Code for the Html will go here",

}

# Creating the Folders 
for folder in folders :
    os.makedirs(folder , exist_ok= True)


# Create Files in Folder 
for file_path , content in files.items():
    with open(file_path,'w') as f:
        f.write(content)


print("WhatsApp Chat Analyzer Folder Structure Created Succesfully")