import logging

from lib.status_code_handler import RequestAndHandle
import time


class Wallapop:
    """ Wallapop Wrapper for search and return all products from query """

    def __init__(self, search, filters, latitude, longitude, order,
                 min_price, max_price):
        self.base_url = "https://api.wallapop.com/api/v3/general/search"
        self.keywords = search
        self.filters = filters
        self.latitude = latitude
        self.longitude = longitude
        self.order_by = order
        self.max_sale_price = max_price
        self.min_sale_price = min_price

        self.delay = 3

    def search_products(self, url: str, old_products: set) -> dict:
        """ Search products given URL """
        new_products = dict()
        for step in range(0, 11):
            time.sleep(self.delay)

            response = RequestAndHandle(url + "&step={}".format(step))
            response_json = response.check_json_response()

            new_products = self.get_web_slug_price(response_json,
                                                   new_products,
                                                   old_products)

        return new_products

    @staticmethod
    def get_web_slug_price(response_js, products_info, old_products):
        """ Given a response, save to dict id -> (web_slug, price) """
        if response_js and len(response_js.get('search_objects')) != 0:
            for product in response_js.get('search_objects'):
                if not product.get('id') in old_products:
                    # Compare if item is in old item saved, due to sort by time
                    products_info[product.get('id')] = \
                        (product.get('web_slug'), product.get('price'))
                else:
                    logging.warning("[-] Last item found ")
                    return products_info

        return products_info

    def generate_url(self) -> str:
        """ Generate search url based on parameters """
        url = "{base}" \
               "?keywords={keywords}" \
               "&filters_source={filters}" \
               "&latitude={latitude}" \
               "&longitude={longitude}" \
               "&order_by={order}".format(base=self.base_url,
                                          keywords=self.keywords,
                                          filters=self.filters,
                                          latitude=self.latitude,
                                          longitude=self.longitude,
                                          order=self.order_by)

        if self.min_sale_price:
            url += "&min_sale_price={}".format(self.min_sale_price)

        if self.max_sale_price:
            url += "&max_sale_price={}".format(self.max_sale_price)

        return url
