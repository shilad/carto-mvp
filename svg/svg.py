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

d = draw.Drawing(4000, 4000, origin="center")
scale()
pd.set_option('display.max_columns', 500)

def find_boundaries():
    country = data.groupby(['countries'], as_index=False).median()
    labels = pd.read_csv("../Results/country_labels.csv", header=None)
    labels.columns = ['countries', 'labels']
    z = country.merge(labels)

    dic = {}
    for index, row in z.iterrows():
        dic[row["countries"]] = [row["x"], row["y"], row["labels"]]

    for key, value in dic.items():
        print(key, " ", value)
    return dic


for i in range(4001):
    title = data.iloc[i, 0]
    x = data.iloc[i, 3]*20
    y = data.iloc[i, 4]*20
    country = data.iloc[i, 5]
    size = data.iloc[i, 7]*50
    d.append(draw.Circle(x, y, size, fill=color[country]))
    if size > 3:
        d.append(draw.Text(title, int(size), x, y)) #, style="font-size: 100px"))

country_label_dic = find_boundaries()
for key, value in country_label_dic.items():
    d.append(draw.Text(value[2], 100, value[0]*20, value[1]*20))

d.setPixelScale(2)  # Set number of pixels per geometry unit
d.saveSvg('example.svg')


