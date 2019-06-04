import csv
from collections import defaultdict

vectors = {}
foodVectors = defaultdict(list)

with open('vectors/original-vectors', encoding="ISO-8859-1") as file:
    for line in file:
        values = line.split()
        vectors[values[0]] = values[1:]
print(vectors['Donald_Trump'])

with open('domain-concept/data.csv', encoding="ISO-8859-1") as data:
    foods = [row[0] for row in csv.reader(data, delimiter='\n')]
    foods[:] = [x.replace(" ", "_") for x in foods]
print(foods)

for vector in vectors:
    if vector in foods:
        foodVectors[vector] = vectors.get(vector)

print(foodVectors.keys())
print(len(foodVectors))

# pd_foodVectors = pd.DataFrame(list(foodVectors.items()))
# pd_foodVectors.columns = ['Article', 'Vectors']
# final_vectors = pd_foodVectors.set_index('Article')
# final_vectors.to_csv("vectors/t-SNE_Vectors")










