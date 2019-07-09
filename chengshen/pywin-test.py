#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: pywin-test.py
@time: 2019/7/9 14:01
@desc:
'''

# 1、python调用短信猫控件，发短信

# ! /usr/bin/env python

# coding=gbk

import sys

import win32com.client

ocxname = 'ShouYan_SmsGate61.Smsgate'

axocx = win32com.client.Dispatch(ocxname)

axocx.CommPort = 8  # 设置COM端口号

axocx.SmsService = '+8613800100500'  # 设置短信服务号码

axocx.Settings = '9600,n,8,1'  # 设置com端口速度

axocx.sn = 'loyin'

c = axocx.Connect(1)  # 连接短信猫或手机

print('连接情况', axocx.Link())

axocx.SendSms('python确实是很好的', '15101021000', 0)  # 发送短信
