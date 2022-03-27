### Part1:收集環保署空氣品質監測資料

## Step1:解析環保署開放資料網頁
import requests
from bs4 import BeautifulSoup
headers = {
    'content-type': 'text/html; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
url = "https://data.epa.gov.tw/dataset/aqx_p_19"
html = requests.get(url=url,headers=headers,timeout=30)
soup = BeautifulSoup(html.content,'html.parser')

## Step2:下載資料壓縮檔
import zipfile, io
import re
import time
for one in soup.select('a[href$=zip]'):
    if re.search(r'aqx_p_19_20[1-2][0-9].*\.zip$', one['href']):
        print(one['href'])
        r = requests.get(one['href'], headers=headers, stream=True, verify=False)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./airdata")
    time.sleep(3)
    
## Step3:從csv檔讀取資料合併成pandas dataframe。只匯入 2010-2021 年資料。
# 讀 2010-2021 年新竹地區(ID:24) PM2.5(ID:33) 資料
# (option) write data to file apx19.csv (without index) for next practise
import glob
import pandas as pd
import numpy as np

files = sorted([f for f in glob.glob("airdata/*.csv") if re.search(r'aqx_p_19_20[1-2][0-9].*\.csv$', f)], reverse=True)
df = pd.concat([pd.read_csv(f, parse_dates=True, encoding='utf8').query('ItemId==33 & SiteId==24') for f in files])
df.reset_index(drop=True, inplace=True)



### Part2:整理及統計資料

## Step1:整理資料
#轉換 MonitorDate 欄位型態，從 object 改為 datetime
df = df[['MonitorDate', 'Concentration']]
df['MonitorDate'] = pd.to_datetime(df['MonitorDate'])
df.info()
#刪除 Concentration 欄位為非數字的 record(列)
df.reset_index(drop=True, inplace=True)
df.drop(df[df['Concentration']=='x'].index, inplace=True)
#轉換 Concentration 欄位型態，從 object 改為 float
df = df.astype({'Concentration':'float'},copy=False)

## Step2:彙總同一年的 PM2.5 資料，計算監測日平均值(同一年加總/該年筆數)。
hc = df[['MonitorDate','Concentration']].groupby(pd.Grouper(key='MonitorDate', freq='1Y')).mean()
hc.head()
hc.info()
hc['year'] = pd.DatetimeIndex(hc.index).year

## Step3:繪製圖表
#create a slightly bigger figure use all the available space
from matplotlib import pyplot as plt
plt.figure(figsize = (10,5))
#XY Plot of year and Concentration
X = hc.index.year
Y = hc['Concentration']
plt.scatter(X,Y)
plt.plot(X,Y)
plt.xticks(np.arange(2010,2023,1), size=12, rotation=70)
# Add axis labels
plt.title('HsinChu PM2.5 Trend')
plt.xlabel('year')
plt.ylabel('PM2.5')
# Increase default font size
plt.rcParams.update({'font.size': 26})
#show plot
plt.show()

### Part3:資料分析與預測

## Step1:線性迴歸
from scipy import stats
slope, intercept, r, p, std_err = stats.linregress(X,Y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, X))

plt.figure(figsize = (10,5))
plt.scatter(X,Y)
plt.plot(X, mymodel)
plt.show()

print('%.2f x + %.2f, r=%f' %(slope,intercept,r))
myfunc(2022)

plt.figure(figsize = (10,5))
model = []
for order in range(1,7):
    p = np.poly1d(np.polyfit(X,Y, order))
    model.append(p)
    plt.scatter(X,Y)
    plt.plot(X, p(X))
plt.show()

#print('%.2f x^3 + %.2f x^2 + %.2f x + %.2f' %tuple(mymodel))
print(mymodel)
mymodel(2022)

R2 = []
for order in range(1,7):
    f = model[order-1]
    R2.append(1-(np.sum((Y-f(x))**2)/np.sum((Y-Y.mean())**2)))

print(R2)
best = R2.index(max(R2))
print(best)
f = model[best]
f(2022)
#print(max(R2))

from sklearn.matrics import r2_score
for order in range(1,4):
    p = model[order-1]
    print(r2_score(Y, p(X)))

## Step2:預測2022年PM2.5平均值
f = np.poly1d(np.polfit(X, Y, 1))
print('The slope of line is %.2f' %f[1])

### R^2 R-squared 判定係數
#迴歸模型的總變異中可被自變數解釋之百分比，判定係數越大迴歸模型的配適度越好。
#一般而言，判定係數大於 0.5 就算不錯了。