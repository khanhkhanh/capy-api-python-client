import requests


class BlacklistClient(object):

    def __init__(self, capy_privatekey, timeout=3):
        self.capy_privatekey = capy_privatekey
        self.timeout = timeout

    def evaluate(self, blacklist_key, capy_ipaddress):
        url = "https://jp.api.capy.me/blacklist/blacklists/%s/evaluate" % blacklist_key
        params = {
            "capy_privatekey": self.capy_privatekey,
            "capy_ipaddress": capy_ipaddress,
        }

        try:
            result = requests.post(url, params, timeout=self.timeout)
            return result
        except:
            return "Connection error"
