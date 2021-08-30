import requests
from pprint import pprint
import time
import json
from time import sleep

#url = 'https://api.vk.com/method/photos.getAll'
#owner_id = 552934290

## this is function to get photo data from vk
class VKphoto_send_to_yadisk():
    def __init__(self):
        self.token = token
        self.data = []
        self.data1 = []
        #self.token_for_yandex = input("please write your token for yandex: ")


    def get_photos_vk_data(self, offset=0, count=50, ):
        #data = []
        #data1 = []
        url_vk = 'https://api.vk.com/method/photos.getAll'
        params = {
            'access_token': token_for_vk,
            'user_id': user_id,
            'extended': 1,
            'offset': offset,
            'count': count,
            'photo_size': 1,
            'no_service_albums': 0,
            'need_hidden': 0,
            'skip_hidden': 0,
            'v': 5.131
        }
        res = requests.get(url_vk, params=params).json()
        rrr = res['response']['items']
        for k in rrr:
            self.data.append(k['likes'])
            self.data1.append(k['sizes'][-1])

        #print(self.data)
        #print(self.data1)

    #def save_photo_from_vk(self):


#yandex disk send there
    def upload(self, file_path: str):

       url = "https://cloud-api.yandex.net:443/"
       url_extra = "v1/disk/resources/upload"
       headers = {
           'content-type' : 'application/json',
            'accept': 'application/json',
            'authorization': f'OAuth {self.token}'
        }
       params = {
            'path': file_path,
            'overwrite': True
        }
       req = requests.get(url + url_extra, params=params, headers=headers)
       pprint(req.json())
       pprint(req)
       uploader_url = req.json()['href']
       #requests.post(url + url_extra, headers=headers, params={'path': 'py44/img.jpeg', 'url': })
       for url in self.data1:
           requests.post(url + url_extra, headers=headers, params={'path': 'py44/img.jpeg', 'url': url['url']})


if __name__ == '__main__':
# Запрашиваем у пользователя данные для работы  in vk
    #tmp_folder = ...
    #user_id = str(input("please give your id: "))
    user_id = 552934290
    token_for_vk = "34f4f11807efbe8c1b82a0850fa70f137c556b7221acde76b2acbf4e7d90fc485f5bd4fdd4ccb496e8e95"
    #user_id = str(input("please give your id: "))

# information for the yandex disk, in order to send it to your disk
    #path_to_file =
    path_to_file = "photo.jpeg"
    token = "AQAAAABXPW06AAdM1-YiAlNVtE3xk5EvzmZuI7U"
    #token_for_yandex = input("please write your token for yandex: ")
    #uploader = VKphoto_send_to_yadisk(token)
    #result = uploader.upload(path_to_file)


pprint(VKphoto_send_to_yadisk().get_photos_vk_data())
pprint(VKphoto_send_to_yadisk())


