import requests
from pprint import pprint
from tqdm import tqdm

import time
import json
from time import sleep

#url = 'https://api.vk.com/method/photos.getAll'
#owner_id = 552934290
#data = []
#data1 = []
#url_list = []
#likes_list = []
## this is function to get photo data from vk
class VKphoto_send_to_yadisk():
    def __init__(self, token_for_vk: str, token: str): #url_list, likes_list
        self.token = token
        self.token_for_vk = token_for_vk
        self.data = []
        self.data1 = []
        self.like_list = []
        self.url_list = []
        self.size = []
        #self.token_for_yandex = input("please write your token for yandex: ")


    def get_photos_vk_data(self, offset=0, count=50):
        #data = []
        #data1 = []
        url_vk = 'https://api.vk.com/method/photos.getAll'
        params = {
            'access_token': self.token_for_vk,
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
        for k in self.data1:
            self.url_list.append(k['url'])
        for k in self.data:
            self.like_list.append(k['user_likes'])
        for size in self.data1:
            self.size.append((size['type']))

        for likes, size in zip(self.like_list, self.size):
            pprint(f'"file_name": "{likes}.jpg""size": "{size}"')

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net:443/"
        url_extra = "v1/disk/resources/upload"
        headers = {
                'content-type': 'application/json',
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
        for likes_count, urll in zip(self.like_list, self.url_list):
            requests.post(url + url_extra, headers=headers,
                          params={'path': f'py44/{likes_count}.jpeg', 'url': urll})

if __name__ == '__main__':
    path_to_file = "photo.jpeg"
    token = input("please write your token for yandex: ")
    user_id = input("please write your user id for vk: ")
    token_for_vk =  input("please write your token for vk: ")
    uploader = VKphoto_send_to_yadisk(token_for_vk, token)
    uploader.get_photos_vk_data()
    uploader.upload(path_to_file)




