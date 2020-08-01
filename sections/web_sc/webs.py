'''import requests

# sending request with URL

URL = 'https://www.thetestingworld.com/'

response = requests.get(URL)

f = open('result.txt','wb')

for data in response.iter_content(10000):
    f.write(data)

f.close()'''

import requests
import bs4
import pandas as pd

URL = 'https://www.thetestingworld.com/'
response = requests.get(URL)

parsed_data=bs4.BeautifulSoup(response.text)

all_links = parsed_data.select('a')

#links = pd.DataFrame([l.getText() for l in all_links])  #get name og the page
links = pd.DataFrame([l.get('href') for l in all_links])   #get href
print(links)