import csv
import pandas as PA
import plotly.figure_factory as ff

df= PA.read_csv("io.csv")
fig1 = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)
fig1.show()

fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist=False)
fig2.show()