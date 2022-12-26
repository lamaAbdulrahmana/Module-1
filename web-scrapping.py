import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 

# to get the name, price, and rating of each product
product_name = [] #List to store name of the product
product_price = [] #List to store price of the product
product_rating = [] #List to store rating of the product

# we get the url from the browser
url = 'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2'
response = requests.get(url)

content = response.content
soup = bs(content,features="lxml")
name = soup.find_all('div', attrs={'class':'_4rR01T'})
price = soup.find_all('div', attrs={'class':'_30jeq3 _1_WHN1'})
rating = soup.find_all('div', attrs={'class':'_3LWZlK'})

for n in name:
    product_name.append(n.text)
    
for p in price:
    product_price.append(p.text)
    
for r in rating:
    product_rating.append(r.text)    
    
df = pd.DataFrame({'Product Name':product_name,'Price':product_price,'Rating':product_rating}) 
df.to_csv('products.csv', index=False, encoding='utf-8')