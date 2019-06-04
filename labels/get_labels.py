import wikipediaapi
import pandas as pd
import numpy as np


def assign_categories(page):
    categories_list = []
    categories = page.categories

    for category in sorted(categories.keys()):
        categories_list.append(category)

    return categories_list


with open("data.csv", "r") as data:
    data = [next(data) for x in range(10)]

    filtered = (line.replace('\n', '') for line in data)
    df = pd.DataFrame(filtered)
    df.rename(index=str, columns={"0": "Titles", "Labels": "Labels"})

    labels = []

    for row in df.head(10).itertuples():
        wiki_wiki = wikipediaapi.Wikipedia('en')
        label = assign_categories(wiki_wiki.page(row._1))
        labels.append(label)

    df["Labels"] = labels
    df.to_csv("data_with_labels.csv", sep=";", encoding='utf-8')
