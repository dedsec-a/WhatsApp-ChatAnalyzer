#PlaceHolder for Pre-processing Functions
import re 
import os 
import string
import numpy as np
import pandas as pd

# Loading the Text Data
# Create a function to load the text data


def load_text_data(file_name):
    """This Function Loads the Text Data from the File path"""
    f = open(f(file_name), "r")
    data = f.read()
    # Calls for Pre-processing the Data
    data = preprocess_text(data)
    return data


def preprocess_text(text):
    """This Fucntion does all the Basic works on the Whatsapp Text Data"""
    # Regex Patter
    pattern = r'\[(\d{2}/\d{2}/\d{2}),\s(\d{1,2}:\d{2}:\d{2})\s?[APMapm]{2}\] ~\s?(.*?):'

    # Finding the Matches 
    matches = re.findall(pattern=pattern , text=text)

    # Creating list for Datetime and users 
    dateTime = []
    users = []

    for match in matches:
        date,time,user_name = match
        dateTime.append(f"{date} {time}")
        users.append(user_name)
        return dateTime, users
    
    # Create a Datagrame 
    df = pd.DataFrame(list(zip(dateTime,users)), columns=["DateTime","Users"])

    # Creating Seperate columns for Time 
    df["Date"] = pd.to_datetime(df["dateTime"]).dt.date
    df["Time"] = pd.to_datetime(df["dateTime"]).dt.time

    # Converting Date into Days Months and Years
    df["Year"] = pd.to_datetime(df["Date"]).dt.year
    df["Month"]= pd.to_datetime(df["Date"]).dt.month
    df["Day"] = pd.to_datetime(df["Date"]).dt.day

    df["Hour"] = pd.to_datetime(df["Time"]).dt.hour
    df["Minute"] = pd.to_datetime(df["Time"]).dt.minute
    df["Second"] = pd.to_datetime(df["Time"]).dt.second

    # Droping the DateTime Column
    df.drop(columns=["DateTime"], inplace=True)

    # Finding the Messages
    pattern_text  =  r'\[\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}:\d{2}\s?[APMapm]{2}\] ~\s?.*?:\s(.*)'

    messages = re.findall(pattern= pattern_text, text=text)

    df["Messages"] = messages

    return df




  


    

