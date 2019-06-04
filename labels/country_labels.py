import pandas as pd
from collections import defaultdict
import ast
import math
import operator

data = pd.read_csv('../Results/final.csv')

# Clean labels
for index, row in data.iterrows():
    new_row = []
    for label in ast.literal_eval(row['Label']):
        entry = label[9:]
        if not entry.startswith('Articles'):
            new_row.append(entry)
    data.at[index, 'Label'] = new_row

print(data.head())

# One dictionary per country, key = label, value = number of occurences in country
label_counts = [defaultdict(int) for x in range(8)]

for index, row in data.iterrows():
    for label in row['Label']:
        label_counts[row['countries']][label] += 1

# One dictionary, key = label, value = number of occurences in total dataset
label_frequency = defaultdict(int)

for index, row in data.iterrows():
    for label in row['Label']:
        label_frequency[label] += 1

# One dictionary per country, key = label, value = TF-IDF score
country_scores = [defaultdict(int) for x in range(8)]

for index, row in data.iterrows():
    for label in row['Label']:
        country_scores[row['countries']][label] = math.log(label_counts[row['countries']][label] + 1.0) / math.log(label_frequency[label] + 10.0)


# One dictionary, key = country, value = country label
country_labels = {}

for x in range(8):
    country_labels[x] = max(country_scores[x].items(), key=operator.itemgetter(1))[0]

print(country_labels)

pd.Series(country_labels).to_csv('../Results/country_labels.csv')

cluster_counts = defaultdict(int)

for index, row in data.iterrows():
    cluster_counts[row['countries']] += 1

print(cluster_counts)