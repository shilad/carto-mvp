import csv
from collections import defaultdict

vectors = {}
foodVectors = defaultdict(list)

with open('vectors/original-vectors.txt', encoding="ISO-8859-1") as file:
    for line in file:
        values = line.split()
        vectors[values[0]] = values[1:]

with open('domain-concept/data.csv', encoding="ISO-8859-1") as data:
    foods = [row[0] for row in csv.reader(data, delimiter='\n')]
    foods[:] = [x.replace(" ", "_") for x in foods]
print(foods)

for vector in vectors:
    if vector in foods:
        foodVectors[vector] = vectors.get(vector)

print(foodVectors.keys())
print(len(foodVectors))










