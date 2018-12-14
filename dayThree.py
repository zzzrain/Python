#!usr/bin/evn python
# coding=utf-8

# QAQ: 调用函数不能传少参数？？


def fnc (data):
    print data
    return


fnc('调用函数')


def info (name, age):
    print '你的名字-----', name
    print '你的年龄-----', age
    return


info('jone', 18)
info(age=18, name='jone')

print '-------------------------------------我是分割线-------------------------------------'


def arr(i, *data):
    print i
    for item in data:
        print item
    return


print '不定长传参：'
arr(1, [5, 6, 7])

noName = lambda x, y: x+y
print '匿名函数——求和', noName(1, 1)

print '-------------------------------------我是分割线-------------------------------------'

gobal = 1


def change(x, y):
    gobal = x+y
    print '局部变量', gobal
    return gobal


change(1, 1)
print '全局变量', gobal
