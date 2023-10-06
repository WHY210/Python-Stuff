import requests
from bs4 import BeautifulSoup
import pandas as pd  
import os
A = {}    
index=1
for i in range(1,11):
    URL='https://www.osha.gov.tw/48110/48461/48517/48553/?Page=%s&PageSize=10' %(i)
    web = requests.get(URL).text    
    soup = BeautifulSoup(web,'html.parser')
    Title = soup.find_all('a')
    for title in Title:
        if "墜落" in str(title.string): 
            A["%d" %index] = [title.string]
            index += 1
df=pd.DataFrame.from_dict(A, orient='index')
path = os.getcwd()
print(path)
df.to_csv(path + '\\file.csv',index=False, encoding='utf_8_sig')