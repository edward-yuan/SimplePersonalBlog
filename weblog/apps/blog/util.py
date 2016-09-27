# encoding: utf-8
import os

#获取路径中的文件名
#
def get_uploadfile_nam(obj):
    path = obj
    name = os.path.basename(path).split('.')[0]
    return name