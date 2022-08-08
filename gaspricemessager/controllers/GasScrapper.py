from bs4 import BeautifulSoup
import requests as req
from lxml import etree
import cfscrape

class GasScrapper:
  def __init__(self, zipcode):
    self.zipcode = zipcode
    url = f'https://www.gasbuddy.com/home?search={zipcode}&fuel=1&maxAge=0&method=all'
    scrapper = cfscrape.create_scraper()
    html = scrapper.get(url).content
    self.soup = BeautifulSoup(html, 'lxml')
  
  def get_prices(self, id):
    data = self.soup.findAll('span', class_=id)
    data = list(map(lambda x: x.text, data))
    data = list(map(lambda x: float(x.replace('$', '')), data))
    return data

  def get_highest_price(self):
    prices = self.get_prices('text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL')
    return max(prices)
  
  def get_lowest_price(self):
    prices = self.get_prices('text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL')
    return min(prices)
    
    
    
if __name__ == "__main__":
  zipcode = input('Enter your zipcode: ')    

  scrapper = GasScrapper(zipcode)

  print(scrapper.get_highest_price())
  print(scrapper.get_lowest_price())