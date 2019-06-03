import csv
import pageviewapi as pv


def get_page_views(food_name):
    """Get number of views of a page for a specific food using PageView API from Wikipedia."""
    page_views = pv.per_article(page=food_name,  project='en.wikipedia', start='20190501', end='20190601',
                                granularity='monthly').get('items')
    views = 0
    for i in range(len(page_views)):
        views += page_views[i].get('views')
    return food_name, views


def concatenate(food_list):
    """Converting a list to a string of food name, concatenate if the name contains a comma."""
    empty = ''
    for page in food_list:
        empty += ',' + page
    return empty


popularity_scores = []


with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for food in csv_reader:
        try:
            if len(food)>1:
                con_cat_page = concatenate(food)
                popularity_scores.append(get_page_views(con_cat_page[1:len(con_cat_page)]))
            elif len(food) ==1:
                popularity_scores.append(get_page_views(food[0]))
        except:
            print(food[0])
            # Things that did not work are:
            # Where's Herb?
            # Hormel/Archive 1
            # Joe's Steaks + Soda Shop
            # 50/50 burger
            # Accrington Stanley
            # Bauhaus books + coffee
            pass

print("writing file")

# create csv file for popularity scores

with open('popularity_scores.csv', 'w') as f:
    for item in popularity_scores:
        popularity_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        popularity_writer.writerow([item[0], item[1]])



