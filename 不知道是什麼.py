from numpy import random
import numpy as np

x = random.choice([3,5,7,9], p = [0.1, 0.3, 0.6, 0.0], size = (100))
x = random.choice([3,5,7,9], p = [0.1, 0.3, 0.6, 0.0], size = (3, 5))

print(x)

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

random.shuffle(arr)

print(arr)

import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

sns.displot([0, 1, 2, 3, 4, 5], hist = False)

plt.show()

x = random.normal(loc = 1, scale = 2, size = (2,3))


import requests
from bs4 import BeautifulSoup
import re

URL = 'http://www.dcard.tw/f'
headers = {

    resp = requests.get(URL, headers = headers)
soup = BeautifulSoup(resp.text, 'html,parser')}


articles = []
for div in soup.find_all('artical', {'role': 'article'}):
    title.div.find("h2").text.strip()
    excert = soup.find('div', re.compile('tgn9uw-4')).text.strip()
    href = div.h2.a['herf']
    articles.append({
        'title':title,
        'excerpt':excerpt
         }
