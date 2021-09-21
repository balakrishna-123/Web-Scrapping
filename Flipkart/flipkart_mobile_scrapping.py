#Flipkart Webscrapping
#importing modules

import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

  #Scrapping the data
url = "https://www.flipkart.com/search?q=mobiles"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")


titles = soup.find_all('div',class_="_4rR01T")

ratings = soup.find_all('div',class_="_3LWZlK")

reviews =soup.find_all('span',class_="_2_R_DZ")

prices = soup.find_all('div',class_="_25b18c")

mt =[]
mr =[]
mre =[]
mp =[]
 
for title,rating,rev,pri in zip(titles,ratings,reviews,prices):
    mt.append(title.text)
    mr.append(rating.text)
    mre.append(rev.text)
    mp.append(pri.text)

#storing the data in csv

data = {'Title':mt,'Ratings':mr,'Reviews':mre,'Price':mp}

model  = pd.DataFrame(data=data)
model.to_csv("mobilesdata.csv")
