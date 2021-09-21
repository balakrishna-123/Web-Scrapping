#importing Modules

import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup



#Url of the website

url  ='https://www.imdb.com/chart/top'



#sending request to website

r = requests.get(url)



#content of the website

soup = BeautifulSoup(r.content,'html.parser')


#creating empty lists for storing the data
movie=[]
link=[]
ratings=[]
img=[]



#scraping and storing the name and link of the movie

title = soup.find_all('td',class_='titleColumn')
for i in title:
    j = i.a.text
    k = i.a['href']
    k = 'https://www.imdb.com/'+k+'?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=5G84WGFCTFN5MP2PDZMX&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'
    movie.append(j)
    link.append(k)

 

#scraping and storing the ratings of the movie
    
rating = soup.find_all('strong')
for i in rating:
    j = i.text
    ratings.append(j)

    

#scraping and storing the image link of the movie
    
image = soup.find_all('img')
for  i in image:
    j = i.get('src')
    img.append(j)


    

#storing the data into csv file
data = {'Movie Name':movie,'Movie Link':link,'Ratings':ratings,'Image Link':img}

df = pd.DataFrame(data=data)
df.to_csv("Movie Ratings by IMDB.csv")
