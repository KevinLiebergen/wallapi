from lib import Telegram
from lib import Wallapop
import logging
import click
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

default_filter = "seo_landing"
default_lat = "40.4893538"
default_long = "-3.6827461"
default_order = "newest"

script_dir = os.path.dirname(os.path.abspath(__file__))
default_telegram_file = os.path.join(script_dir, 'config/telegram.yaml')


@click.command()
@click.option('-search', required=True, help='Keywords to search')
@click.option('-filters', default=default_filter,
              help="Default parameter on all queries ")
@click.option('-longitude', default=default_long,
              help="Longitude to search, default={}".format(default_long))
@click.option('-latitude', default=default_lat,
              help="Latitude to search, default={}".format(default_lat))
@click.option('-order', default=default_order,
              help="Order mode. Default {}".format(default_order))
@click.option('-min-price', required=False, help="Min price to search")
@click.option('-max-price', required=False, help="Max price to search")
@click.option('-teleg', required=False, default=default_telegram_file,
              help="Telegram config file")
def cli(search, filters, longitude, latitude, order, teleg,
        min_price=None, max_price=None):
    """ Parameter handler, create objects and pass them to main """
    wallapop = Wallapop(search, filters, latitude, longitude, order, min_price,
                        max_price)
    if teleg:
        telegram = Telegram(teleg)
    else:
        telegram = None

    main(wallapop, telegram)


def load_saved_products() -> set:
    """ Load saved products """
    last_ids = set()
    path = os.path.join(script_dir, 'config/last_ids.txt')

    if os.path.exists(path):
        last_ids_fd = open(path, 'r')
        for id in last_ids_fd.readlines():
            last_ids.add(id.strip())

    return last_ids


def save_products(new_products: dict):
    """ Save new products found """
    path = os.path.join(script_dir, 'config/last_ids.txt')
    last_ids_fd = open(path, 'a')
    for product_id in new_products.keys():
        last_ids_fd.write("{}\n".format(product_id))


def main(walla, telegram):
    """ Search products and print them out """
    url = walla.generate_url()
    old_products = load_saved_products()
    new_products = walla.search_products(url, old_products)
    save_products(new_products)

    logging.warning("{} new products found".format(len(new_products)))

    if telegram:
        telegram.send_messages(new_products.values())
    else:
        print(new_products)


if __name__ == '__main__':
    cli()
