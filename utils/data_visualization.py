import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
from collections import Counter
from logger import logging
from logger import exception
import sys
import nltk
from nltk.corpus import stopwords
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Creating a Function to show the Activity trend of the user

def activity_trend(df , frequency = "M"):
    """ This function Takes Dataframe as input and Retruns the Month Or Week wise activity trend of a user in the 
    chat or the group Chat"""

    # making a Copy of the Dataframe
    df_engrouped = df.copy()

    month_mapping = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }

    df_engrouped["Month"] = df_engrouped["Month"].map(month_mapping).fillna(df_engrouped["Month"]).astype(int)

    #Concattinating the  Date and Time back together
    df_engrouped["DateTime"] = pd.to_datetime(df_engrouped[['Year','Month','Day','Hour','Minute','Second']])


    # Grouping the Data on the Basic of Choosen Frequency 
    if(frequency == "M"):
        trend_data = df_engrouped.groupby(df_engrouped["DateTime"].dt.to_period("M").size().reset_index(name = "Message Count"))
        trend_data["DateTime"] = trend_data["DateTime"].astype(str)
        title = "Monthly User Activity Trend"
    elif(frequency == "W"):
        trend_data = df_engrouped.groupby(df_engrouped["DateTime"].dt.toperiod("W").sixe().reset_index(name = "Message Count"))
        trend_data["DateTime"] = trend_data["DateTime"].astype(str)
        title = "Weekly User Activity Trend"
    else:
        print("Unspuuorted Value Type ")
        raise ValueError("Frequency should be either M or W")
     
    logging.info("Creating the Activity Trend Plot")

    # Ploting the Given Data 
    fig = px.line(
        data_frame= trend_data,
        x= "DateTime",
        y= "Message Count",
        title = title,
        markers=True,
        labels={
            "DateTime": "Date",
            "Message Count": "Message Count"
        },
        template = "plotly_white"
    )

    fig.update_traces(line= dict(color = "blue", width= 2))
    fig.update_layout(xaxis_title = "Date", yaxis_title = "Message Count")
    fig.show()

# Creating a function for showing Weekly and Montlhy Active users

def activeUsers(df,frequency = "M", no_of_users = 10):
    """ This function takes a Dataframe and Freqency as input and gives a barplot stating 
    the most active user either Month wise or Week Wise""" 

    df_engrouped = df.copy()

    # Mapping the months 
    months_maping = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    } 

    df_engrouped["Month"] = df_engrouped["Month"].map(months_maping).fillna(df_engrouped["Month"]).astype(int)

    # Creating a Datetime Column 
    df_engrouped["DateTime"]= pd.to_datetime(df_engrouped[["Year","Month","Day","Hour","Minute","Second"]])

    # Grouping the Data based on the users
    if(frequency == "M"):
        active_users = df_engrouped.groupby(["Users", df_engrouped["DateTime"].dt.to_period("M")]).size().reset_index(name= "Message Count")
        active_users["DateTime"] = active_users["DateTime"].astype(str)
        top_users = active_users.groupby("Users")["Message Count"].sum().sort_values(ascending=False).head(no_of_users).reset_index(name="Message Count")  
        title = "Monthly Active Users"

    elif(frequency == "W"):
        active_user = df_engrouped.groupby(["Users",df_engrouped["DateTime"].dt.to_period("W")]).size().reset_index(name="weekly active users")
        active_user["DateTime"] = active_users["DateTime"].astype(str)
        top_users = active_users.groupby("Users")["Message Count"].sum().sort_values(ascending=False).head(no_of_users).reset_index(name="Message Count")
        title = "Weekly Active Users"
    else:
        print("Unspupported Value Type")
        raise ValueError("Frequency should be either M or W")
    logging.info("Creating the Active Users Plot")

    fig = px.bar(
        top_users,
        x= "Users",
        u= "Message Count",
        title = title,
        template= "plotly_white",
        labels={
            "Users": "Users",
            "Message Count": "Message Count"
        },
        color = "Users"
    )
    fig.update_layout(xaxis_title="User", yaxis_title="No. of Messages")
    fig.show()



nltk.download("stopwords")
nltk.download("punkt")

def preprocess_text(text):
    # 1. Convert text to lowercase
    text = text.lower()
    
    # 2. Remove links, digits, and punctuation
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)  # Remove links
    text = re.sub(r"\d+", "", text)  # Remove digits
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation

    # 3. Tokenize text
    words = word_tokenize(text)

    # 4. Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]

    # Return processed text in a format suitable for WordCloud
    return " ".join(filtered_words)
    


# Function to crerate a Word Cloud 
def create_wordcloud(df):
    """ This Function takes a DataFrame as input and then returns the Word Cloud for the given Corpus
    Word Cloud - It a a Visual Representation of the Most Common Words in the Corpus"""

    # Joining all the messages 
    text = " ".join(df["Messages"].dropna().astype(str))

    # PreProcessing the Text for the Word Cloud
    text = preprocess_text(text)
    
    # Creating the WordCloud 
    wordcloud = WordCloud(
        width=1000,
        height=500,
        background_color="white",
        colormap="Set2",
        max_words=200,
        contour_color='black',
        contour_width=3,
    ).generate(text)

    # Display the WordCloud
    plt.figure(figsize=(15, 7))
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.show()
    logging.info("Creating the WordCloud")

 


    