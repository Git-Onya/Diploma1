import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # Получение ссылки на загрузку файлов на Ядиск
    def get_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    # Загрузка файла в указанную папку на Ядиске
    def upload(self, file_path: str, filename):
        href = self.get_link(file_path=file_path).get("href", "")
        print(href)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        return response.status_code

    # Функция принимает сформированный при закачке из профиля ВК список файлов, берет из него имена файлов и загружает все на Ядиск
    def upload_from_list(self, file_path, files_list):
        count = 1
        for file in files_list:
            filename = file["file_name"]
            res = self.upload(file_path, filename)
            # Лог загрузки файлов
            if res == 201:
                print(f'Uploaded {count} of {len(files_list)} files')
            count += 1

    # Создает папку на Ядиске
    def make_dir(self, dir_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        params = {'path': dir_name}
        headers = self.get_headers()
        res = requests.put(url=url, headers=headers, params=params)
