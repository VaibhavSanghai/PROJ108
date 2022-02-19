import plotly_express as p
import plotly.figure_factory as f
import csv
import pandas as pd

df = pd.read_csv("data.csv")
fig = f.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)
fig.show()