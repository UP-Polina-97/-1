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
        self.like_list = []
        self.url_list = []
        self.size = []
        self.name = []


    def get_photos_vk_data(self, count=5):
        url_vk = 'https://api.vk.com/method/photos.get'
        params = {
            'access_token': self.token_for_vk,
            'user_id': user_id,
            'album_id': 'profile',
            'extended': 1,
            'count': count,
            'v': 5.131
        } #'photo_size': 1, 'extended': 1,
        res = requests.get(url_vk, params=params).json()
        rrr = res['response']['items']
        pprint(rrr)

        for k in rrr:
            self.url_list.append(k['sizes'][-1]['url'])
            self.size.append(k['sizes'][-1]['type'])
            if k['likes'] in self.like_list:
                self.name.append(k['date'])
            else:
                self.name.append(k['likes']['count'])
                self.like_list.append(k['likes'])

        #print("Получение информации о фото из ВК завершено.\n  \nНачата загрузка фото на Яндекс.Диск...")

    def upload(self):
        url = "https://cloud-api.yandex.net:443/"
        url_extra = "v1/disk/resources/upload"
        headers = {
                'content-type': 'application/json',
                'accept': 'application/json',
                'authorization': f'OAuth {self.token}'
            }
        for name, urll in zip(self.name, self.url_list):
            requests.post(url + url_extra, headers=headers,
                          params={'path': f'py44/{name}.json', 'url': urll})

        #print("Фото ... загружено \n ... \nЗагрузка фото на Яндекс.Диск завершена")


if __name__ == '__main__':
    token = input("please write your token for yandex: ")
    user_id = input("please write your user id for vk: ")
    token_for_vk = input("please write your token for vk: ")
    uploader = VKphoto_send_to_yadisk(token_for_vk, token)
    print('Получение информации о фото из ВК...')
    uploader.get_photos_vk_data()
    print("Получение информации о фото из ВК завершено.\n  \nНачата загрузка фото на Яндекс.Диск...")
    uploader.upload()
    print("Фото ... загружено \n ... \nЗагрузка фото на Яндекс.Диск завершена")




