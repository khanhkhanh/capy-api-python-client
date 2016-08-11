import requests


class RiskbaseClient(object):

    def __init__(self, capy_privatekey, timeout=3):
        self.capy_privatekey = capy_privatekey
        self.timeout = timeout

    def authenticate(self, riskbase_key, capy_data):
        url = "https://jp.api.capy.me/riskbase/v0.1/riskbases/%s/evaluate" % riskbase_key
        params = {
            "capy_privatekey": self.capy_privatekey,
            "capy_data": capy_data
        }

        try:
            result = requests.post(url, params, timeout=self.timeout)
            return result
        except:
            return "Connection error"
