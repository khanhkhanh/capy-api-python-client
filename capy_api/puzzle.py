import requests


class PuzzleClient(object):

    def __init__(self, capy_privatekey, timeout=3):
        self.capy_privatekey = capy_privatekey
        self.timeout = timeout

    def verify(self, capy_challengekey, capy_answer):
        url = "https://jp.api.capy.me/puzzle/verify"
        params = {
            "capy_challengekey": capy_challengekey,
            "capy_privatekey": self.capy_privatekey,
            "capy_answer": capy_answer
        }

        try:
            result = requests.post(url, params, timeout=self.timeout)
            return result
        except:
            return "Connection error"
