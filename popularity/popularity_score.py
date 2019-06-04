import csv
import pageviewapi as pv


def get_page_views(start_date, end_date, page_name, granularity):
    """Get number of views of a page for a specific food using PageView API from Wikipedia."""
    page_views = pv.per_article(page=page_name, project='en.wikipedia', start=start_date, end=end_date,
                                granularity=granularity).get('items')
    views = 0
    for i in range(len(page_views)):
        views += page_views[i].get('views')
    return page_name, views


def concatenate(food_list):
    """Converting a list to a string of food name, concatenate if the name contains a comma."""
    empty = ''
    for page in food_list:
        empty += ',' + page
    return empty


popularity_scores = []

# print(get_page_views('20190501', '20190601', 'Bauhaus books + coffee', 'monthly'))
print(popularity_scores.append(get_page_views('20180601', '20190601', food[0], 'monthly')))
with open('../domain-concept/data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for food in csv_reader:
        try:
            if len(food) > 1:
                con_cat_page = concatenate(food)
                popularity_scores.append(get_page_views('20180601', '20190601', con_cat_page[1:len(con_cat_page)], 'monthly'))
            elif len(food) == 1:
                popularity_scores.append(get_page_views('20180601', '20190601', food[0], 'monthly'))
        except:
            print(food[0])
            # Things that did not work are:
            # Where's Herb?
            # Hormel/Archive 1
            # 50/50 burger
            # Accrington Stanley
            pass

print("writing file")

# create csv file for popularity scores

with open('2018_popularity_scores.csv', 'w') as f:
    for item in popularity_scores:
        popularity_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        popularity_writer.writerow([item[0], item[1]])



