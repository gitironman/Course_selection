from lib import common
from conf import settings
from core.cls import student
from core.cls import course
import os


class Admin:
    operate_list = [('创建课程', 'create_course'),
                    ('创建学生账号', 'create_student'),
                    ('查看所有课程', 'show_courses'),
                    ('查看所有学生', 'show_students'),
                    ('查看所有学生的选课情况', 'show_students_choices'),
                    ('创建管理员', 'admin_create'),
                    ('退出程序', 'quit')]

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    @staticmethod
    def create_course():
        print('\033[1;36;0m欢迎进入创建课程界面\033[0m')
        name = input('\033[1;36;0m请输入课程名：\033[0m').strip()
        price = input('\033[1;36;0m请输入价格：\033[0m').strip()
        period = input('\033[1;36;0m请输入周期：\033[0m').strip()
        teacher = input('\033[1;36;0m请输入老师：\033[0m').strip()
        course_obj = course.Course(name, price, period, teacher)
        common.pickle_write(settings.course_dbpath, name, course_obj)

    @staticmethod
    def create_student():
        print('\033[1;36;0m欢迎进入创建学生账号界面\033[0m')
        usr = input('\033[1;36;0m请输入用户名：\033[0m').strip()
        pwd = input('\033[1;36;0m请输入密码：\033[0m').strip()
        pwd = common.pwd_md5(usr, pwd)
        stu_obj = student.Student(usr, pwd)
        common.pickle_write(settings.student_dbpath, usr, stu_obj)

    @staticmethod
    def show_courses():
        print('\033[1;36;0m欢迎进入查看所有课程界面\033[0m')
        course_list = os.listdir(settings.course_dbpath)
        for index, course_name in enumerate(course_list, 1):
            obj = common.pickle_read(settings.course_dbpath, course_name)
            print('{}、 课程名：{}，价格：{}，周期：{}，老师：{}'.format(index, course_name, obj.price, obj.period, obj.teacher))

    @staticmethod
    def show_students():
        print('\033[1;36;0m欢迎进入查看所有学生界面\033[0m')
        stu_list = os.listdir(settings.student_dbpath)
        for index, stu in enumerate(stu_list, 1):
            print('{}、 学生：{}'.format(index, stu))

    @staticmethod
    def show_students_choices():
        print('\033[1;36;0m欢迎进入查看所有学生的选课情况界面\033[0m')
        stu_list = os.listdir(settings.student_dbpath)
        for index, stu in enumerate(stu_list, 1):
            obj = common.pickle_read(settings.student_dbpath, stu)
            print('{}、 学生：{}，所选课程：{}'.format(index, stu, ','.join([i.name for i in obj.course])))

    @staticmethod
    def admin_create():
        print('\033[1;36;0m欢迎进入创建管理员界面\033[0m')
        common.admin_create()

    @staticmethod
    def quit():
        print('\033[1;31;0m已退出\033[0m')
        quit()
