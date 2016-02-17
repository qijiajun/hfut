# -*- coding:utf-8 -*-
from __future__ import unicode_literals, division

from logging import Logger, WARNING, StreamHandler, Formatter

hfut_stu_lib_logger = Logger('hfut_stu_lib', level=WARNING)

sh = StreamHandler()
fmt = Formatter('%(levelname)s:%(filename)s-%(lineno)d %(funcName)s: %(message)s')
sh.setFormatter(fmt)
hfut_stu_lib_logger.addHandler(sh)
