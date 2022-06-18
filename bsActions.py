from urllib.request import urlopen
from bs4 import BeautifulSoup

def extract_data(main_heading, html):
    item_data = {}
    soup = BeautifulSoup(html, 'lxml')
    rows = soup.findChildren('div', 'sub-cate-row')
    i = 0
    ii = 0
    category ={}
    for row in rows:
        items = row.findChildren('dl')

        for item in items:
            sub_heading = item.dt.a.string
            sub_categories = []
            sub_items = item.dd.find_all('a')
            
            for sub_item in sub_items:
                # print(heading , '---->', sub_item.string)
                sub_categories.append(sub_item.string)
            category[i] = {
                'sub-heading': sub_heading,
                'sub_categories': sub_categories
                }
            i = i+1
    item_data = {
        'main-category':main_heading,
        'categories': category
        }
            
    return item_data

