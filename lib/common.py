from core.cls import admin
from core.cls import student
from conf import settings
import pickle
import hashlib
import os


def identity_judgment(obj):
    if isinstance(obj, admin.Admin):
        return 'admin'
    elif isinstance(obj, student.Student):
        return 'student'


def admin_create():
    usr = input('\033[1;36;0m请输入用户名：\033[0m').strip()
    pwd = input('\033[1;36;0m请输入密码：\033[0m').strip()
    pwd = pwd_md5(usr, pwd)
    admin_obj = admin.Admin(usr, pwd)
    pickle_write(settings.admin_dbpath, usr, admin_obj)


def pwd_md5(usr, pwd):
    usr = (lambda x: x[-1] + '学校名称' + str(len(x)))(usr)
    ret = hashlib.md5(usr.encode('utf-8'))
    ret.update(pwd.encode('utf-8'))
    return ret.hexdigest()


def pickle_write(path, filename, obj):
    if not os.path.isdir(path):
        os.mkdir(path)
    with open(path + filename, mode='wb') as f1:
        pickle.dump(obj, f1)


def pickle_read(path, filename):
    with open(path + filename, mode='rb') as f2:
        obj = pickle.load(f2)
    return obj
