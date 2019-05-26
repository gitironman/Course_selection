#! usr/bin/env python
# -*- coding: utf-8 -*-
# __author: iamironman
# @file: starts
# @time: 2019年01月21日
# @email: 875674794@qq.com

import os
import sys
from core import src
# from lib import common  # db下没有管理员账号时 需要用这个创建

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

if __name__ == '__main__':
        # common.admin_create()  # db下没有管理员账号时 需要用这个创建
        src.run()
