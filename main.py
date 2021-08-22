import requests
from pprint import pprint
import time
import json
from time import sleep
#token = '34f4f11807efbe8c1b82a0850fa70f137c556b7221acde76b2acbf4e7d90fc485f5bd4fdd4ccb496e8e95'
#url = 'https://api.vk.com/method/photos.getAll'
#owner_id = 552934290

## this is function to get photo data from vk
class VKphoto_send_to_yadisk():
    owner_id = input("please give your id: ")
    token_for_ya = input("please write your token for yandex: ")
    url = 'https://api.vk.com/method/photos.getAll'
    token_for_vk = '34f4f11807efbe8c1b82a0850fa70f137c556b7221acde76b2acbf4e7d90fc485f5bd4fdd4ccb496e8e95'
    data = []
    data1 = []

    def get_photos_vk_data(offset=0, count=50):
        params = {
            'access_token': token_for_vk,
            'user_id': owner_id,
            'extended': 1,
            'offset': offset,
            'count': count,
            'photo_size': 1,
            'no_service_albums': 0,
            'need_hidden': 0,
            'skip_hidden': 0,
            'v': 5.131
        }
        res = requests.get(url, params=params).json()
        rrr = res['response']['items']
        for k in rrr:
            data.append(k['likes'])
            data1.append(k['sizes'][-1])

    def __init__(self, token: str):
        self.token = token

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
       with open(file_path, 'rb') as file:
            files = requests.put(uploader_url, data=file)
       print(files)

if __name__ == '__main__':
    #path_to_file =
    #loop for different file
    for k in data1:
        path_to_file = (k['url'])
    token = token_for_ya
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

## progress bar function 1


#def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
#	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
#	filledLength = int(length * iteration // total)
#	bar = fill * filledLength + '-' * (length - filledLength)
#	print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
#	if iteration == total:
#		print()
