from YaDi import YaUploader
from VkPhoto import VkPhoto
import os
import system

if __name__ == '__main__':
    v = VkPhoto(system.vk_token, '5.131')
    os.mkdir(system.id)
    photos_list = v.download_photo(system.id)
    ya = YaUploader(system.ya_token)
    ya.make_dir(system.id)
    ya.upload_from_list(system.id, photos_list)
