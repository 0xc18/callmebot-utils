import requests

BASEURL='https://api.callmebot.com/whatsapp.php'

class Whatsapp:
    def __init__(self,API_KEY:str,PHONE:str):
        self._API_KEY = API_KEY
        self._PHONE = PHONE

    def send_text(self,text):
        params = {
                'apikey' : self._API_KEY,
                'phone' : self._PHONE,
                'text' : text,
                }
        response = requests.get(BASEURL,params=params)
        return response.text
