import json
from urllib.request import urlopen
from bs4 import BeautifulSoup


url2 = 'https://www.aliexpress.com/all-wholesale-products.html'

page = urlopen(url2)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'xml')

data = {}
i = 0

elements = soup.find_all('div', 'item util-clearfix')
for el in elements:
    head = el.h3.a.string
    
    sub_elements = el.find_all('ul', 'sub-item-cont util-clearfix')
    for sub in sub_elements:
        listItem = sub.find_all('a')
        sub_categories = []
        for item in listItem:
            sub_category = item.string
            sub_categories.append(sub_category)
        data[i] = {
            'category': head,
            'sub_categories': sub_categories
        }   
        i=i+1
        
    
with open('categories.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



