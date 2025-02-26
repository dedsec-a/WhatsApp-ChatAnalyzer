# Placeholder for Sentiment Analysis Logic
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification , pipeline
import pandas as pd
import numpy as np
import plotly.express as px


model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)

# Create a Sentiment Analysis Pipeline

sentiment_analyis = pipeline("sentiment-analysis", model= model , tokenizer= tokenizer,device=-1)

def get_sentiment(df):
    """ This function takes the Dataframe as imput and then Extracts the Texts from it and does some pre_processing on the
    text and returns the Sentiment of the Text and add it's to the DataFrame"""
    # Extracting the Messages from the Dataframe
    # Analyze the sentiment of each message
    sentiment = df["Message"].apply(lambda x: sentiment_analyis(x)[0])
    sentiment = pd.DataFrame(list(sentiment))
# Concatenate the sentiment with the original DataFrame 
    df_sentiment = pd.concat([df, sentiment], axis=1)

    return df_sentiment

# Ploting the Bargraph for the Sentiment Analysis
def plot_sentiment_analysis(df):
    # Grouping the Data
    value_count = df["label"].value_counts().reset_index()
    value_count.columns = ["Sentiment", "Count"]
    # Plotting the Bar Graph
    fig = px.bar(
        value_count,
        x="Sentiment",
        y="Count",
        title="Sentiment Analysis",
        template="plotly_white",
        labels={"Sentiment": "Sentiment", "Count": "No. of Messages"},
        color="Sentiment"  # Adds different colors for each sentiment
    )
    fig.update_layout(xaxis_title="Sentiment", yaxis_title="No. of Messages")
    fig.show()


    
    