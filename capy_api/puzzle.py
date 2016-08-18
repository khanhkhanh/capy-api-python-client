from tasks import verify


class PuzzleClient(object):
    url = "https://jp.api.capy.me/puzzle/verify"

    def __init__(self, capy_privatekey, timeout=3):
        self.capy_privatekey = capy_privatekey
        self.timeout = timeout

    def verify(self, capy_challengekey, capy_answer):
        verify(self.capy_privatekey, capy_challengekey, capy_answer, self.url, self.timeout)

    def verify_async(self, capy_challengekey, capy_answer):
        verify.apply_async(self.capy_privatekey, capy_challengekey, capy_answer, self.url, self.timeout)


client = PuzzleClient("a")
response = "fuck"

client.verify_async("b", "c")
print response
