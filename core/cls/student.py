from lib import common
from conf import settings
import os


class Student:
    operate_list = [
        ('查看可选课程', 'show_courses'),
        ('选择课程', 'choose_course'),
        ('查看所选课程', 'show_selected_courses'),
        ('退出程序', 'quit')]

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.course = []

    @staticmethod
    def show_courses():
        print('\033[1;34;0m欢迎进入查看可选课程界面\033[0m')
        course_list = os.listdir(settings.course_dbpath)
        for index, course in enumerate(course_list, 1):
            obj = common.pickle_read(settings.course_dbpath, course)
            print('{}、 课程名：{}，价格：{}，周期：{}，老师：{}'.format(index, course, obj.price, obj.period, obj.teacher))

    def choose_course(self):
        self.show_courses()
        print('\033[1;34;0m欢迎进入选课界面\033[0m')
        course_list = os.listdir(settings.course_dbpath)
        try:
            choice = int(input('请输入序号：').strip())
        except Exception as e:
            print('\033[1;31;0m{}\033[0m'.format(e))
        else:
            course_obj = common.pickle_read(settings.course_dbpath, course_list[choice - 1])
            self.course.append(course_obj)
            common.pickle_write(settings.student_dbpath, self.name, self)

    def show_selected_courses(self):
        print('\033[1;34;0m欢迎进入查看所选课程界面\033[0m')
        for index, courses in enumerate(self.course, 1):
            print('{}、 课程名：{}，价格：{}，周期：{}，老师：{}'.format(index, courses.name, courses.price, courses.period,
                                                        courses.teacher))

    @staticmethod
    def quit():
        print('\033[1;31;0m已退出\033[0m')
        quit()
