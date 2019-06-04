import pandas as pd

food_vectors = pd.read_csv('../vectors/t-SNE_Vectors')
food_clusters = pd.read_csv('../Clustering/food_clusters.csv')

final_df = food_vectors.join(food_clusters, how='outer')
final_df.columns = ['Articles', 'Vectors','Cluster_group']

print(final_df.head())