import pandas as pd
import csv

current = pd.read_csv('../combined_xy_clustered.csv')




popularity = pd.read_csv('../popularity/2018_popularity_scores.csv', header=None)
popularity = popularity.replace(" ", "_",regex=True)

popularity.columns = ['Article', 'pop_score']

current_pop = current.merge(popularity, how="inner")

export = current_pop.to_csv(r'../Results/results.csv', index=False)
