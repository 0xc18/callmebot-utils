import requests

BASE_URL = 'https://api.callmebot.com/facebook/send.php'

def upload_uguu(filepath:str):
    with open(filepath,'rb') as r:
        files = {'files[]':r}
        response = requests.post('https://uguu.se/upload',files=files)
        return response.json().get('files',[{}])[0].get('url','')

class Facebook:
    def __init__(self,API_KEY : str):
        self._API_KEY = API_KEY

    def send_text(self,text : str):
        params={
                'apikey' : self._API_KEY,
                'text' : text,
                }
        response = requests.get(BASE_URL,params=params)
        return response.text

    def send_image_by_url(self,image_url : str):
        params={
                'apikey' : self._API_KEY,
                'image' : image_url,
                }
        response = requests.get(BASE_URL,params=params)
        return response.text

    def send_image(self,image_path):
        image_url = upload_uguu(image_path)
        return self.send_image_by_url(image_url)

