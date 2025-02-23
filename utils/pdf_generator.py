# Logic for Pdf Generation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import fpdf as FPDF
from utils.data_visualization import create_wordcloud

x = [1,2,3,4]
y = [12,23,45,56]

df = pd.DataFrame(x,y)

create_wordcloud(df=df)