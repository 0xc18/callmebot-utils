import requests

BASE_URL = 'https://signal.callmebot.com/signal/send.php'

class Signal:
    def __init__(self,API_KEY: str, PHONE: str):
        self._API_KEY = API_KEY
        self._PHONE = PHONE

    def send_text(self,text: str):
        params={
                'apikey' : self._API_KEY,
                'phone' : self._PHONE,
                'text' : text
                }
        response = requests.get(BASE_URL,params=params)
        return response.text
