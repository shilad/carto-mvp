import numpy as np
import pandas as pd
import numpy as np
import ast

# We import sklearn.
import sklearn
from sklearn.manifold import TSNE


def str_to_list(string):
    string = ast.literal_eval(string)
    [n.strip() for n in string]

df = pd.read_csv("./vectors/t-SNE_Vectors.csv")
vectors = np.array(df["Vectors"])
float_lst = []

for x in vectors:
    x = ast.literal_eval(x)
    x = np.array([n.strip() for n in x])
    y = x.astype(np.float)
    float_lst.append(y)

embedded = TSNE().fit_transform(float_lst)

embedded_df = pd.DataFrame(data=embedded)
embedded_df.to_csv("xy_embedded.csv", index=False)