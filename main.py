import requests
import json
from pprint import pprint


class VKphoto_send_to_yadisk():
    def __init__(self, token_for_vk: str, token: str):
        self.token = token
        self.token_for_vk = token_for_vk
        self.like_list = []
        self.url_list = []
        self.size = []
        self.name = []
        self.for_print = []

    def get_photos_vk_data(self, count=5):
        url_vk = 'https://api.vk.com/method/photos.get'
        params = {
            'access_token': self.token_for_vk,
            'user_id': user_id,
            'album_id': 'profile',
            'extended': 1,
            'count': count,
            'v': 5.131
        }
        res = requests.get(url_vk, params=params).json()
        rrr = res['response']['items']

        for k in rrr:
            self.url_list.append(k['sizes'][-1]['url'])
            self.size.append(k['sizes'][-1]['type'])
            if k['likes'] in self.like_list:
                self.name.append(k['date'])
            else:
                self.name.append(k['likes']['count'])
                self.like_list.append(k['likes'])

    def upload(self):
        url = "https://cloud-api.yandex.net:443/"
        url_extra = "v1/disk/resources/upload"
        url_extra_folder = "v1/disk/resources"
        headers = {
                'accept': 'application/json',
                'authorization': f'OAuth {self.token}'
            }

        for name, size in zip(self.name, self.size):
            self.for_print.append({"file_name": f"{name}.jpg","size": f"{size}"})

        with open('data_for_photos.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.for_print, json_file, ensure_ascii=False, indent= 4)


        requests.put(url + url_extra_folder, headers=headers, params={'path': 'photos'})

        for name, urll in zip(self.name, self.url_list):
            requests.post(url + url_extra, headers=headers,
                          params={'path': f'photos/{name}.jpg', 'url': urll})

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