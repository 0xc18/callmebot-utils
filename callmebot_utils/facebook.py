import requests

BASE_URL = 'https://api.callmebot.com/facebook/send.php'

class Facebook:
    def __init__(self,API_KEY : str):
        self.API_KEY = API_KEY

    def send_text(self,text : str):
        params={
                'apikey' : self.API_KEY,
                'text' : text,
                }
        response = requests.get(BASE_URL,params=params)
        return response.text

    def send_image(self,image_url : str):
        params={
                'apikey' : self.API_KEY,
                'image' : image_url,
                }
        response = requests.get(BASE_URL,params=params)
        return response.text
