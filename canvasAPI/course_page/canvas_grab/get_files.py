from requests import request
from canvasapi import Canvas
import datetime
import os
import requests
class File():
    def __init__(self, display_name, id, url, size, created_at, updated_at, locked):
        self.display_name = display_name
        self.id = id
        self.url = url
        self.size = size
        self.created_at = created_at
        self.updated_at = updated_at
        self.locked = locked

    def __str__(self):
        return self.display_name

    def __eq__(self, other):
        if self.id == other.id and self.display_name == other.display_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.id < other.id:
            return True
        else:
            return False

    def get_status(self):
        self.msg = ''
        if self.locked:
            self.msg = '已锁定'
        else:
            if self.updated_at - self.created_at > datetime.timedelta(hours=1):
                self.msg = '已更新'
            else:
                self.msg = '正常'

def get_file_dict(course_id):
    API_URL = 'https://oc.sjtu.edu.cn'
    API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
    canvas = Canvas(API_URL, API_KEY)
    course = canvas.get_course(course_id)
    file_dict = {}
    file_list = []
    format = '%Y-%m-%dT%H:%M:%SZ'
    for file in course.get_files():
        display_name = file.display_name
        id = file.id
        url = file.url
        size = file.size

        created_at = file.created_at
        created_at = datetime.datetime.strptime(created_at, format)
        created_at += datetime.timedelta(hours=8)

        updated_at = file.updated_at
        updated_at = datetime.datetime.strptime(updated_at, format)
        updated_at += datetime.timedelta(hours=8)

        locked = file.locked
        f = File(display_name,id,url,size,created_at,updated_at,locked)
        f.get_status()
        file_dict[id] = f
        file_list.append(f)
    return file_dict, file_list

def download_file(file_obj, directory):
    file_directory = os.path.join(directory,file_obj.display_name)
    r = requests.get(file_obj.url)
    with open(file_directory,'wb+') as f:
        f.write(r.content)



