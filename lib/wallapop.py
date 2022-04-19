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

    def search_products(self, url: str, products_info: dict) -> dict:
        """ Search products given URL """
        for step in range(0, 11):
            time.sleep(self.delay)

            response = RequestAndHandle(url + "&step={}".format(step))
            response_json = response.check_json_response()

            products_info = self.get_web_slug_price(response_json,
                                                    products_info)

        return products_info

    @staticmethod
    def get_web_slug_price(response_js, products_info):
        if response_js and len(response_js.get('search_objects')) != 0:
            for product in response_js.get('search_objects'):
                if not products_info.get(product.get('id')):
                    products_info[product.get('id')] = \
                        (product.get('web_slug'), product.get('price'))
                else:
                    # Found last item saved, due to we sort by time
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
