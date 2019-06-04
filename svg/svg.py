import numpy as np
import pandas as pd
import drawSvg as draw

data = pd.read_csv("../Results/final.csv").iloc[:, 1:]
color = ["red", "blue", "green", "yellow", "brown", "orange", "cyan", "black"]

def scale():
    scale_lst = []
    max = data.loc[data['pop_score'].idxmax()]['pop_score']
    min = data.loc[data['pop_score'].idxmin()]['pop_score']

    for index, row in data.iterrows():
        scale_pop_val = (row['pop_score']-min)/(max-min)
        scale_lst.append(scale_pop_val)

    data["scale"] = scale_lst

d = draw.Drawing(2000, 2000, origin="center")
scale()
pd.set_option('display.max_columns', 500)

print(data.head())
print(data.columns)
for i in range(4001):
    x = data.iloc[i, 3]*8
    y = data.iloc[i, 4]*8
    country = data.iloc[i, 5]
    size = data.iloc[i, 7]*50
    d.append(draw.Circle(x, y, size, fill=color[country]))

d.setPixelScale(2)  # Set number of pixels per geometry unit
d.saveSvg('example.svg')

