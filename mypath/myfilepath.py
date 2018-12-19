# -*- coding: utf-8 -*-

import os

class Mypath(object):
    def __init__(self, file):
        '''
        :param file:文件夹名称，如果没有的就创建
        '''
        self.file = file
        dir_name = os.path.join(os.getcwd(), self.file)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def file_path(self):
        '''
        :return:文件夹路径
        '''
        return os.path.join(os.getcwd(), self.file)

    def filename_path(self, file_name):
        '''
        :param file_name:文件名
        :return:文件名及文件路径，元组
        '''
        return file_name, os.path.join(self.file_path(), file_name)

