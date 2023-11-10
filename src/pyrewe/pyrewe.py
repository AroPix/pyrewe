import json

import cloudscraper
import requests
from bs4 import BeautifulSoup


class rewe():
    def __init__(self, cookie=None, base_url="https://shop.rewe.de"):
        self.base_url = base_url
        self.request = cloudscraper.create_scraper()
        if cookie is not None:
            self.cookie = cookie
            self.request.headers = {
                'Cookie': self.cookie,
            }
        self.headers = {
            'authority': 'shop.rewe.de',
            'accept': 'application/json',
            'accept-language': 'de-DE,de;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://shop.rewe.de',
            'pragma': 'no-cache',
            'referer': 'https://shop.rewe.de/p/minusl-h-vollmilch-3-5-1l/3736989',
            'sec-ch-ua': '"Chromium";v="118", "Brave";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-application-id': 'rewe-basket',
            'x-device-accept': 'application/vnd.com.rewe.digital.basket-ui+json',
            'x-origin': 'AddToBasketV2',
            'cookie': self.cookie
        }

        self.basket_version = None
        self.basket = None
        self.basket_id = None
        self.get_basket_id()

    def get_products(self, query: str) -> dict:
        url = self.base_url + "/api/suggestions?q=" + query
        response = self.request.request("GET", url)

        return response.json()

    def set_basket_quantity(self, listingId: str, quantity: int) -> tuple[dict, int]:
        url = self.base_url + "/api/basket/quantity"
        payload = json.dumps({
            "listingId": listingId,
            "quantity": quantity,
        })

        response = self.request.post(url, data=payload, headers=self.headers)
        self.basket_version = response.json()['version']
        self.basket_id = response.json()['id']
        self.get_basket()

        return response.json(), response.status_code

    def add_to_basket(self, listingId: str, quantity: int):
        self.get_basket_id()
        self.get_basket()
        calc = quantity
        if 'merchantBaskets' in self.basket:
            if len(self.basket['merchantBaskets']) != 0:
                for product in self.basket['merchantBaskets'][0]['lineItems']:
                    if listingId == product['listing']['id']:
                        calc += product['quantity']

        return self.set_basket_quantity(listingId, calc)

    def change_basket_quantity(self, listingId: str, quantity: int) -> tuple[dict, int]:
        return self.set_basket_quantity(listingId, quantity)

    def remove_from_basket(self, listingId: str) -> tuple[dict, int]:
        return self.set_basket_quantity(listingId, 0)

    def get_basket_version(self) -> int:
        response = self.get_basket(self.basket_id)[0]
        self.basket_version = response['version']
        return response['version']

    def get_basket(self) -> tuple[dict, int]:
        url = self.base_url + "/api/internal/baskets/" + self.basket_id
        response = self.request.get(url, headers=self.headers)
        self.basket = response.json()
        return response.json(), response.status_code

    def get_basket_id(self) -> str:
        response = self.set_basket_quantity("13-4001052136019-f75dc7b0-fe2b-3e7c-b49b-3c9826eff156", 0)[0]
        self.basket_id = response['id']
        return response['id']


def get_product_info_link(product_link: str):
    """Don't use, might trigger Cloudflare"""
    url = product_link
    scraper = cloudscraper.create_scraper()

    html = scraper.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        product_info = soup.find_all('script', type='application/json', id=lambda value: value and value.startswith("pdpr-propstore"))[0].text
    except:
        print(html)
    return json.loads(product_info)

def get_product_infos(listingIds: list) -> dict:
    url = "https://shop.rewe.de/api/product-tiles?serviceTypes=PICKUP&listingIds="
    for listingId in listingIds:
        url += listingId + ','
    url = url[:-1]

    requests.get(url)

    return requests.get(url).json()

def off_info(gtin: str):
    response = requests.get(f"https://world.openfoodfacts.net/api/v3/product/{gtin}?lc=de&cc=de&tags_lc=de&fields=attribute_groups")
    return response.json()
