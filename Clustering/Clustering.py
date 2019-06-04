from sklearn.cluster import KMeans
import pandas as pd
import  numpy as np

food_vectors = pd.read_csv('../vectors/t-SNE_Vectors')
print(type(list(food_vectors['Vectors'][0])))
vectors_array = np.array(list(food_vectors['Vectors'][0]), dtype=np.float)
print(vectors_array.head())


