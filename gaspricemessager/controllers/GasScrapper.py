from bs4 import BeautifulSoup
import cfscrape

class GasScrapper:
  def __init__(self, zipcode):
    self.zipcode = zipcode
    self._create()
    
  def _create(self):
    self.soup = self.make_soup(self.zipcode)
    self.prices = self._get_prices('text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL')
    
  def make_soup(self, zipcode):
    url = f'https://www.gasbuddy.com/home?search={zipcode}&fuel=1&maxAge=0&method=all'
    scrapper = cfscrape.create_scraper()
    html = scrapper.get(url).content
    return BeautifulSoup(html, 'lxml')
  
  def _get_prices(self, id):
    data = self.soup.findAll('span', class_=id)
    data = list(map(lambda x: x.text, data))
    data = list(map(lambda x: float(x.replace('$', '')), data))
    return data

  def get_highest_price(self):
    return max(self.prices)
  
  def get_lowest_price(self):
    return min(self.prices)
  
  def get_average_price(self):
    return round(sum(self.prices) / len(self.prices), 2)
  
  def set_zipcode(self, zipcode):
    self.zipcode = zipcode
    self._create()
    
    
    
    
if __name__ == "__main__":
  zipcode = input('Enter your zipcode: ')    

  scrapper = GasScrapper(zipcode)
  print(scrapper.get_highest_price())
  print(scrapper.get_lowest_price())
  print(scrapper.get_average_price())
  
  zipcode = input('Enter your zipcode: ')
  
  scrapper.set_zipcode(zipcode)
  print(scrapper.get_highest_price())
  print(scrapper.get_lowest_price())
  print(scrapper.get_average_price())
  
  
  
  