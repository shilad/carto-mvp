import wikipedia as wp
import csv
import pageviewapi as pv
views = 0
def get_PageViews(food_name):
    pageviews = pv.per_article(end='20180701', page=food_name, start='20180601', project='en.wikipedia',
                               granularity='monthly').get('items')
    views = 0
    for i in range(len(pageviews)):
        views += pageviews[i].get('views')
    return (food_name, views)

def concatenate(list):
    empty = ''
    for page in list:
        empty+= ',' + page
    return empty



popularity_scores = []
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for food in csv_reader:
        try:
            if len(food)>1:
                con_cat_page = concatenate(food)
                popularity_scores.append(get_PageViews(con_cat_page[1:len(con_cat_page)]))
            elif len(food) ==1:
                popularity_scores.append(get_PageViews(food[0]))
        except:
            pass

print("writing file")

with open('popularity_scores.csv', 'w') as f:
    for item in popularity_scores:
        popularity_writer = csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        popularity_writer.writerow([item[0],item[1]])



