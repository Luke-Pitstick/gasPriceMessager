from bs4 import BeautifulSoup
import cfscrape



class GasScraper:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.ids = {
            "div": "GenericStationListItem-module__stationListItem___3Jmn4",
            "h3": "header__header3___1b1oq header__header___1zII0 header__midnight___1tdCQ header__snug___lRSNK StationDisplay-module__stationNameHeader___1A2q8",
            "price": "text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL",
            "address": "StationDisplay-module__address___2_c7v",
        }
        self.__create()

    def __create(self):
        self.soup = self.__make_soup(self.zipcode)
        self.prices = self.__create_prices()
        self.price_values = list(map(lambda x: x["price"], self.prices.values()))

    def __make_soup(self, zipcode):
        url = (
            f"https://www.gasbuddy.com/home?search={zipcode}&fuel=1&maxAge=0&method=all"
        )
        scrapper = cfscrape.create_scraper()
        html = scrapper.get(url).content
        return BeautifulSoup(html, "lxml")

    def __create_prices(self):
        divs = self.soup.findAll("div", class_=self.ids["div"])
        len_divs = len(divs)
        prices = {}

        for div in divs:
            h3 = div.find("h3", class_=self.ids["h3"])
            gasStation = h3.a.text
            price = div.find("span", class_=self.ids["price"]).text
            address = div.find("div", class_=self.ids["address"]).text

            for i in range(len_divs):
                if price != "---":
                    prices[gasStation] = {
                        "price": float(price[1:]),
                        "address": address,
                    }

        return prices
        
    def get_prices(self):
        return self.prices

    def get_highest_price(self):
        maximum = max(self.price_values)
        index = self.price_values.index(maximum)
        station = list(self.prices.keys())[index]
        address = self.prices[station]["address"]
        address_link = f"https://www.google.com/maps/search/?api=1&query={address.replace(' ', '+')}"

        return {
            station: {
                "price": maximum,
                "address": address,
                "address_link": address_link,
            }
        }

    def get_lowest_price(self):
        minimum = min(self.price_values)
        index = self.price_values.index(minimum)
        station = list(self.prices.keys())[index]
        address = self.prices[station]["address"]
        address_link = f"https://www.google.com/maps/search/?api=1&query={address.replace(' ', '+')}"

        return {
            station: {
                "price": minimum,
                "address": address,
                "address_link": address_link,
            }
        }

    def get_average_price(self):
        average = round(sum(self.price_values) / len(self.price_values), 2)
        return average

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode
        self._create()


if __name__ == "__main__":
    zipcode = input("Enter your zipcode: ")

    scraper = GasScraper(zipcode)

    print(scraper.get_lowest_price())
    print()
    print(scraper.get_highest_price())
    print()
    print(scraper.get_average_price())
