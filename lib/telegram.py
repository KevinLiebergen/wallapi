import logging
import telebot
import time
import yaml


def _greet(file):
    logging.warning("[-] Reading Telegram config file from {} ".format(file))


class Telegram:
    def __init__(self, path):
        with open(path) as yaml_file:
            _greet(yaml_file.name)

            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
            self.token = data['credentials']['token']
            self.ch_id = data['credentials']['ch_id']

        self.tb = telebot.TeleBot(self.token)
        self.item_url = "https://es.wallapop.com/item/"
        self.delay_error = 30
        self.delay = 5

    def send_messages(self, url: list):
        """ Given list of messages, print to Telegram channel """
        for message in url:
            time.sleep(self.delay)
            try:
                self.tb.send_message(self.ch_id, "{}€ {}".format(message[1],
                                                                 self.item_url +
                                                                 message[0]))
            except telebot.apihelper.ApiTelegramException:
                logging.warning("A request to the Telegram API was "
                                "unsuccessful. Error code: 429. Description: "
                                "Too Many Requests")
                time.sleep(self.delay_error)
