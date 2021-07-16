import json
from YaDi import YaUploader
from VkPhoto import VkPhoto

if __name__ == '__main__':
    with open('vk_token.txt', encoding='utf-8') as file:
        token = file.read().strip()
    v = VkPhoto(token, '5.131')
    photos_list = v.download_photo('552934290')  # список для загрузки берется из метода класса или загружается из json?
    # with open('photos_list.json', 'r') as f:
    #     photos = json.load(f)
    with open('ya_token.txt', encoding='utf-8') as file:
        ya_token = file.read().strip()
    ya = YaUploader(ya_token)
    ya.make_dir('Photos')
    ya.upload_from_list('Photos', photos_list)
