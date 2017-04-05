'''
Created on 2017年4月5日

@author: HL
'''
import os
from datetime import datetime
import shutil
class photo_classify(object):
    '''
    1. make object
    path = path you want
    obj = photo_classify(path)
    2.use get_picture_info to get path and date information
    3.use move_all_images_to_targate to move photos
    4.Check all done.
    '''
    get_path = ""
    photo_info = {}
    def __init__(self, path_of_photo):
        self.get_path = path_of_photo
    def __str__(self, *args, **kwargs):
        string = self.get_path + " have already been classified."
        return string
    def get_picture_info(self):
        filenames = os.listdir(self.get_path)
        for file in filenames:
            path = os.path.join(self.get_path,file)
            if os.path.isdir(path):
                continue
            else:
                path = os.path.join(self.get_path,file)
                timestamp = os.path.getmtime(path)
                time = datetime.fromtimestamp(timestamp)
                photo_time = time.strftime("%Y-%m-%d")
                self.photo_info[path] = photo_time
        print(self.photo_info)
    def is_image(self,img_file):
        if os.path.isdir(img_file):
            return False
        return img_file[-4:] in ['.jpg','.dng','.png']
    def move_all_images_to_targate(self):
        for photo,date in self.photo_info.items():
            targetPath = os.path.join(self.get_path,date)
            #make new dir
            if not os.path.exists(targetPath):
                os.mkdir(targetPath)
            #move photo to new place by date
            shutil.move(photo, targetPath)
            
if __name__ == '__main__':
    test = photo_classify('D:\手機照片')
    test.get_picture_info()
    test.move_all_images_to_targate()

            
        