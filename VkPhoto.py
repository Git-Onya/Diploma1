import requests
import json


class VkPhoto:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    # Получение списка фото всех размеров из альбома profile
    def get_photos_list(self, id):
        photos_url = self.url + 'photos.get'
        get_photo_params = {
            'owner_id': id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1
        }
        resp = requests.get(photos_url, params={**self.params, **get_photo_params})
        return resp.json()['response']['items']

    # переименование файла в случае совпадения кол-ва лайков, загрузка файла на жесткий диск
    def download_photo(self, id):
        photos = self.get_photos_list(id)
        photos_list = []
        for photo in photos:
            size = photo['sizes'][-1]['type']
            url = photo['sizes'][-1]['url']
            name = f'{photo["likes"]["count"]}.jpg'
            res = requests.get(url)
            for photos in photos_list:
                count = 1
                if name in photos["file_name"]:
                    name = f'{photo["likes"]["count"]}_{count}.jpg'
                    count += 1
            with open(name, 'wb') as f:
                f.write(res.content)
            # скачивает в папку нормально, но не берет из папки при загрузке на Ядиск. пишет, что неправильный формат имени
            # with open(f'{id}/{name}', 'wb') as f:
            #     f.write(res.content)
            photos_list.append({"file_name": name, "size": size})
        with open('photos_list.json', 'w', encoding='utf-8') as f:
            json.dump(photos_list, f, indent=1)
        return photos_list
