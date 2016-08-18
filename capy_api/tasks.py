import requests
from celery import Celery


app = Celery('', include=['puzzle', 'avatar', 'blacklist', 'riskbase'], backend='amqp', broker='amqp://guest@localhost//')


@app.task
def verify(capy_privatekey, capy_challengekey, capy_answer, url, timeout):
    params = {
        "capy_challengekey": capy_challengekey,
        "capy_privatekey": capy_privatekey,
        "capy_answer": capy_answer
    }

    try:
        result = requests.post(url, params, timeout=timeout)
        print("???")
        return result
    except:
        return "Connection error"
