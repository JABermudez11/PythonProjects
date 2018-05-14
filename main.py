from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#put page into a variable
my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# grab page
uClient = uReq(my_url)

# reads the page and puts it into a variable
page_html = uClient.read()

#closes page
uClient.close()

# put into a variable, our website as a html parser
page_soup = soup(page_html, "html.parser")

page_soup.findAll("div",{"class":"item-container"})

