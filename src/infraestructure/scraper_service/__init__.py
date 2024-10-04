import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


class ScraperService:
    def __init__(self):
        pass

    def scrape_products(self, url):
        content = self._get_page(url)
        return self._get_products(content)

    @staticmethod
    def _get_page(url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)

            page.wait_for_selector('#gallery-layout-container')
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            content = page.content()
            browser.close()

        soup = BeautifulSoup(content, 'html.parser')
        return soup

    @staticmethod
    def _get_products(content):
        products = []
        container = content.find('div', {"id": "gallery-layout-container"})
        if container:
            articles = container.find_all('article', {"class": "vtex-product-summary-2-x-element"}, limit=15)
            for article in articles:
                prices = article.find_all('div', {"class": "tiendasjumboqaio-jumbo-minicart-2-x-pp_container"})
                name = article.find('span', {"class": "vtex-product-summary-2-x-brandName"}).text
                price = None
                promo_price = None
                # If there is a promo price
                if len(prices) > 1:
                    promo_price = prices[0].text
                    price = prices[1].text
                else:
                    price = prices[0].text
                    promo_price = prices[0].text
                product = {
                    'price': price,
                    'promo_price': promo_price,
                    'name': name.strip()
                }
                products.append(product)
        return products
