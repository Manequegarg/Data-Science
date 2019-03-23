import requests
from bs4 import BeautifulSoup as bsoup
url = 'http://www.grover.com/de-en/phones-and-tablets/smartphones'
# Html parsing
page = requests.get(url)
soup = bsoup(page.text, "html.parser")
# Fetching Data
containers =soup.findAll("div",{"class":"categoryListingGridItem"})
#
filename = "products.csv"
f= open(filename, "w")
header= "Name; Details; Price\n"
f.write(header)
#

for Product in containers:
 try:
  Name = Product.find('div', {"class" : "productCard__name"})
  Product_Name = Name.string
  #
  Details = Product.find('div',{"class":"productCard__caption"})
  Product_Details = Details.string
  #
  Price = Product.find('div',{"class":"storeShowPrice"})
  Product_Price = Price.text
  #
  print(Product_Name)
  print(Product_Details)
  print(Product_Price)
 
  
 except (IOError, AttributeError):
  pass
 f.write(Product_Name + ";" + Product_Details + ";" + Product_Price + "\n")
f.close()