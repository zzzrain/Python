#!/usr/bin/evn python
# -*- coding: UTF-8 -*-

print '打印语句：', 'hello word'

noOne = 0
noTwo = 1

if noOne:
    print '判断语句：', '樽的'
elif noTwo:
    print '判断语句：', '贾的'
else:
    print '判断语句：', '樽贾不分'

print '-------------------------------------我是分割线-------------------------------------'

print '数字类型：', noOne, noTwo

string = 'Sakura is pretty and cuties y'
print '字符串类型：' + string[0], (string[0:6] + string[7:-1])*2

tiny = ['E', 'J', 'H']
tinyList = ['Eun Jung', 'Ji Yeon', 'Hyo Min']
tinyList[2] = 'Hai Min'
tinyListS = tiny + tinyList
print '列表类型（可改变）：', tinyListS, tinyListS[3]

tuples = ('Q', 'B', 'S')
tupleList = ('Qri', 'Bo Ram', 'So Yeon')
# tupleList[2] = 'BoBo' #元组只读，重新赋值报错
tupleListS = tuples + tupleList
print '元组类型（不可变）：', tupleListS, tupleListS[5]

print '-------------------------------------我是分割线-------------------------------------'

dicts = {}
dicts['Q'] = 'Qri'
dicts['B'] = 'Bo Ram'
dicts['S'] = 'So Yeon'
dicts['H'] = 'Hyo Min'
dicts['E'] = 'Eun Jung'
dicts['J'] = 'Ji Yeon'
print '字典类型（对象）：', dicts
print '字典（键）：', dicts.keys()
print '字典（值）：', dicts.values()

print '-------------------------------------我是分割线-------------------------------------'

print '数字处理：'
print '整点', int(3.14)
print '整型', long(3.14)
print '浮点', float(3.14)
print '复数', complex(3.14)

print '-------------------------------------我是分割线-------------------------------------'

print '字典==>字符串', str(dicts)
print '字典==>字符串', repr(dicts)
print '列表==>元组', tuple(tiny)
print '元祖==>列表', list(tuples)

print '-------------------------------------我是分割线-------------------------------------'

nameA = set('Sasaki')
nameB = set('Nozomi')
print '集合关系：'
print '交集', nameA & nameB
print '并集', nameA | nameB
print '差集', nameA - nameB
print '差集', nameB - nameA

print '-------------------------------------我是分割线-------------------------------------'

print '构造字典', dict([('Q', 'Qri'), ['B', 'Bo'], ('S', 'So')])
print 'zip方法:', dict(zip(['Q', 'B', 'S'], ('Qri', 'Bo', 'So')))

print '-------------------------------------我是分割线-------------------------------------'

print '不可变集合', frozenset(range(10))
print '不可变集合',  frozenset('Sakura')
