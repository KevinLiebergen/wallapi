import logging
import requests


class RequestAndHandle:
    """ Check if request URL and handle server responses are correct """
    def __init__(self, url: str):
        self.response = requests.get(url)

    def check_json_response(self) -> dict:
        """ Return JSON response whether it is correct or not """
        if self.is_good_response():
            struct = self.response.json()
        else:
            struct = None
        return struct

    def is_good_response(self) -> bool:
        if self.response.status_code == 200:
            return True
        else:
            if self.response.status_code == 400:
                logging.warning("[-] Bad Request -- Your request is invalid.")
            elif self.response.status_code == 401:
                logging.warning("[-] Unauthorized -- Your API key is wrong.")
            elif self.response.status_code == 403:
                logging.warning("[-] Forbidden -- The kitten requested is "
                                "hidden for administrators only.")
            elif self.response.status_code == 404:
                logging.warning("[-] Not Found -- The specified kitten could "
                                "not be found.")
            elif self.response.status_code == 405:
                logging.warning("[-] Method Not Allowed -- You tried to access "
                                "a kitten with an invalid method.")
            elif self.response.status_code == 406:
                logging.warning("[-] Not Acceptable -- You requested a format "
                                "that isn't json.")
            elif self.response.status_code == 410:
                logging.warning("[-] Gone -- The kitten requested has been "
                                "removed from our servers.")
            elif self.response.status_code == 418:
                logging.warning("[-] I'm a teapot.")
            elif self.response.status_code == 429:
                logging.warning("[-] Too Many Requests -- You're requesting "
                                "too many kittens! Slow down!")
            elif self.response.status_code == 500:
                logging.warning("[-] Internal Server Error -- We had a problem "
                                "with our server. Try again later.")
            elif self.response.status_code == 503:
                logging.warning("[-] Service Unavailable -- We're temporarily "
                                "offline for maintenance. Please try again "
                                "later.")
            else:
                logging.warning("[-] Unknown response: "
                                "{}".format(self.response.status_code))
            return False

