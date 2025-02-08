# Placeholder for Data Visulasation Functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = [1,2,3,4,5]
y = [20,15,20,19,56]

def plot_values(x,y):
    plt.figure(figsize=(10,6))
    plt.plot(x,y,marker = "o")
    plt.title("Sample plot")
    plt.xlabel("Sample Distribution")
    plt.ylabel("Sample Values")
    plt.grid(True)
    
    plt.show()