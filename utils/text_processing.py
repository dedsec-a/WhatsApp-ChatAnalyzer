#PlaceHolder for Pre-processing Functions
import re 
import os 
import string
import numpy as np
import pandas as pd

# Loading the Text Data
# Create a function to load the text data



import re
import pandas as pd

import re
import pandas as pd

def preprocess_text(text):
    """Processes WhatsApp chat data into structured format."""

    # Corrected regex pattern for extracting Date, Time, and Usernames
    pattern = r'\[(\d{2}/\d{2}/\d{4}),\s(\d{1,2}:\d{2}:\d{2}\s?[APMapm]{2})\] (.*?): (.*)'

    # Finding matches
    matches = re.findall(pattern, text)

    # If no matches are found, return an empty DataFrame
    if not matches:
        print("⚠️ No messages found! Check the file format or regex.")
        return pd.DataFrame()

    # Creating a DataFrame
    df = pd.DataFrame(matches, columns=["Date", "Time", "Users", "Messages"])

    # Convert DateTime to pandas datetime format
    df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

    # Extract Date and Time Separately
    df["Date"] = df["DateTime"].dt.date
    df["Time"] = df["DateTime"].dt.time

    # Extract Year, Month, and Day
    df["Year"] = df["DateTime"].dt.year
    df["Month"] = df["DateTime"].dt.month
    df["Day"] = df["DateTime"].dt.day

    # Extract Hour, Minute, and Second
    df["Hour"] = df["DateTime"].dt.hour
    df["Minute"] = df["DateTime"].dt.minute
    df["Second"] = df["DateTime"].dt.second

    # Drop DateTime column (if not needed)
    df.drop(columns=["DateTime"], inplace=True)

    return df






  


    

