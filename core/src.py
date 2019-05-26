from core import cls
from lib import common
from conf import settings
import os


def login():
    usr = input('\033[1;34;0m请输入用户名：\033[0m').strip()
    if os.path.isfile(os.path.join(settings.admin_dbpath, usr)):
        obj = common.pickle_read(settings.admin_dbpath, usr)
    elif os.path.isfile(os.path.join(settings.student_dbpath, usr)):
        obj = common.pickle_read(settings.student_dbpath, usr)
    else:
        return {'flag': None}
    pwd1 = input('\033[1;34;0m请输入密码：\033[0m').strip()
    pwd2 = common.pwd_md5(usr, pwd1)
    if pwd2 == obj.pwd:
        return {'flag': True, 'obj': obj}
    else:
        return {'flag': False}


def run():
    print('\033[1;34;0m欢迎进入选课系统登录页面\033[0m')
    ret = login()
    if ret['flag']:
        print('\033[1;34;0m登录成功\033[0m')
        if common.identity_judgment(ret['obj']) == 'admin':
            while 1:
                print('\033[1;36;0m欢迎进入管理员界面\033[0m')
                for i, v in enumerate(cls.Admin.operate_list, 1):
                    print(i, v[0])
                try:
                    num = int(input('请输入序号：').strip())
                    method = cls.Admin.operate_list[num - 1][1]
                    if hasattr(ret['obj'], method):
                        getattr(ret['obj'], method)()
                except Exception as e:
                    print('\033[1;31;0m{}\033[0m'.format(e))

        elif common.identity_judgment(ret['obj']) == 'student':
            while 1:
                print('\033[1;34;0m欢迎进入学生界面\033[0m')
                for i, v in enumerate(cls.Student.operate_list, 1):
                    print(i, v[0])
                try:
                    num = int(input('请输入序号：').strip())
                except Exception as e:
                    print('\033[1;31;0m{}\033[0m'.format(e))
                else:
                    method = cls.Student.operate_list[num - 1][1]
                    if hasattr(ret['obj'], method):
                        getattr(ret['obj'], method)()
    elif ret['flag'] is False:
        print('\033[1;31;0m密码错误\033[0m')
    else:
        print('\033[1;31;0m用户名不存在\033[0m')
