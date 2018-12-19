#!usr/bin/evn python
# coding=utf-8

import time
import calendar
import random

for num in range(1, 3):
    print num

nameA = ['Q', 'B', 'S', 'E', 'J', 'H']
nameB = ('Qri', 'Bo Ram', 'So Yeon', 'Eun Jung', 'Ji Yeon', 'Hyo Min')

print '-------------------------------------打印列表-------------------------------------'
for keyA in nameA:
    print keyA

print '-------------------------------------打印元组-------------------------------------'
for keyB in nameB:
    print keyB

arrs = [13, 3, 1, 4, 15, 10]
arrs.append(10)
arrs.sort()

print '-------------------------------------我是分割线-------------------------------------'

# 列表属性&&方法
print 'append() && sort()：', arrs
print '统计出现频率 count()：', arrs.count(10)
print '列表的长度 len()：', len(arrs)
print '列表最大值 max()：', max(arrs)
print '列表最小值 min()：', min(arrs)
print '列表转元组 tuple()：', tuple(arrs)

arrsEX = ['a', 'b', 'c']
print '比较列表 cmp()：', cmp(arrs, arrsEX)

arrs.extend(arrsEX)
print '合并列表 arr()：', arrs

# 列表其他方法： index insert pop remove

print '-------------------------------------我是分割线-------------------------------------'

print '时间戳', time.time()
print '全时间', time.localtime()
print '本地时间', time.asctime()
print '时间格式', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print '月历', calendar.month(2018, 3)

print '随机数', random.random()
print '固定随机数', random.choice(['Q', 'B', 'S', 'E', 'J', 'H'])
print '范围随机数', int(random.uniform(1,10))
