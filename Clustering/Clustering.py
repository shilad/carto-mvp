from sklearn.cluster import KMeans
import pandas as pd
import  numpy as np
import ast
import csv


food_vectors = pd.read_csv('../vectors/t-SNE_Vectors')
#print(type(list(food_vectors['Vectors'][0])))
#print(vectors_array.head())
# print(np.array(food_vectors['Vectors'][1:len(food_vectors['Vectors'])-1]).astype(np.float))
vectors = []
for i in range(0, len(food_vectors['Vectors'])):
    list_food = ast.literal_eval(food_vectors['Vectors'][i])
    vectors.append(np.array(list_food).astype(np.float))


food_matrix = np.stack(vectors)

kmeans = KMeans().fit(food_matrix)

with open('food_clusters.csv', 'w') as f:
    for item in kmeans.labels_:
        print(item)
        label_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        label_writer.writerow([item])

#print(len(kmeans.labels_))