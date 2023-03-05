import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

base_link = 'https://biodelly.fi/'
url = 'https://biodelly.fi/collections/miehille'
res = requests.get(url)

all_link = []
all_data = []
soup = bs(res.text, 'html.parser')

links = soup.find_all('a', {'class': 'product-info__caption'})

for link in links:
    product_link = link.get('href')
    all_link.append(base_link+product_link)
# print(len(all_link))

for data in all_link:
    res2 = requests.get(data)
    soup2 = bs(res2.text, 'html.parser')
    product_title = soup2.find('h1', {'class': 'product_name'}).text
    price = soup2.find('span', {'class': 'current_price'}).text
    image_link = soup2.find('div', {'class': 'image__container'})
    image = image_link.find('img').get('src')
    product_details = soup2.find('div', {'class': 'description bottom'})
    product_de = product_details.find('p').text
    product_information = {
        'product_title' : product_title,
        'price' : price,
        'image_link' : image,
        'product_details' : product_de


    }
    all_data.append(product_information)
    # print(all_data)
data_information = pd.DataFrame(all_data, columns=['product_title', 'price', 'image_link', 'product_details'])
data_information.to_csv('datas.csv', index=False, encoding='utf-8')
print(data_information)