import requests
from pprint import pprint
from tqdm import tqdm

import time
import json
from time import sleep


class VKphoto_send_to_yadisk():
    def __init__(self, token_for_vk: str, token: str): #url_list, likes_list
        self.token = token
        self.token_for_vk = token_for_vk
        self.data1 = []
        self.like_list = []
        self.url_list = []
        self.size = []
        self.name = []


    def get_photos_vk_data(self, offset=0, count=50):

        print('Получение информации о фото из ВК...')
        url_vk = 'https://api.vk.com/method/photos.get'
        params = {
            'access_token': self.token_for_vk,
            'user_id': user_id,
            'album_id': 'profile',
            'photo_ids': '',
            'rev': 1,
            'extended': 1,
            'feed_type': '',
            'feed': '',
            'photo_size': 1,
            'offset': offset,
            'count': count,
            'v': 5.131
        }
        res = requests.get(url_vk, params=params).json()
        rrr = res['response']['items']

        for k in rrr:
            self.data1.append(k['sizes'][-1])

        for k in self.data1:
            self.url_list.append(k['url'])
            self.size.append(k['type'])

        for photo in rrr:
            if photo['likes'] in self.like_list:
                self.name.append(photo['date'])
            else:
                self.name.append(photo['likes']['count'])
                self.like_list.append(photo['likes'])






        print("Получение информации о фото из ВК завершено.\n  \nНачата загрузка фото на Яндекс.Диск...")

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
        for name, urll in zip(self.name, self.url_list):
            requests.post(url + url_extra, headers=headers,
                          params={'path': f'py44/{name}.jpeg', 'url': urll})

        print("Фото ... загружено \n ... \nЗагрузка фото на Яндекс.Диск завершена")


if __name__ == '__main__':
    path_to_file = "photo.jpeg"
    token = input("please write your token for yandex: ")
    user_id = input("please write your user id for vk: ")
    token_for_vk = input("please write your token for vk: ")
    uploader = VKphoto_send_to_yadisk(token_for_vk, token)
    uploader.get_photos_vk_data()
    uploader.upload(path_to_file)




