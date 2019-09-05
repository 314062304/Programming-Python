#!usr/bin/python
# coding=utf-8

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue jones', 45, 40000, 'hardware']

# 使用list
print('使用list：')
print(bob[0], sue[2])               # 获取姓名，薪水

print(bob[0].split()[-1])           # bob姓什么

sue[2] *= 1.25                      # 给sue加薪25%
print(sue)
print('\n')


# 数据库列表
print('数据库列表：')
people = [bob, sue]                 # 引用列表的列表
for person in people:
    print(person)

print(people[1][0])

for person in people:               # 打印姓氏
    print(person[0].split()[-1])
    person[2] *= 1.20               # 涨20%的薪水

for person in people:               # 检查新的薪酬
    print(person[2])

pays = [person[2] for person in people]     # 收集薪酬信息
print(pays)

pays = map((lambda x: x[2]), people)        # 同上（map是3.X中的生成器）
print(list(pays))

print(sum(person[2] for person in people))  # 生成器表达式, sum为内建函数

people.append(['Tom', 50, 0, None])         # 向数据库中添加记录，使用append和extend足够
print(len(people))
print(people)
print(people[-1][0])
print('\n')


# Field标签
print('Field标签：')
NAME, AGE, PAY = range(3)           # 0, 1和2
bob = ['Bob Smith', 42, 10000]
print(bob[NAME])
print(PAY, bob[PAY])

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
    print(person[0][1], person[2][1])

print([person[0][1] for person in people])

for person in people:
    print(person[0][1].split()[-1])
    person[2][1] *= 1.10

for person in people:
    print(person[2])

for person in people:
    for (name, value) in person:
        if name == 'name':      # 寻找特定的字段
            print(value)

def field(record, label):
    for(fname, fvlaue) in record:
        if fname == label:
            return fvlaue
            print(field(bob, 'name'))
            print(field(sue, 'pay'))


for rec in people:
    print(field(rec, 'age'))

print('\n')


# 使用字典
print('使用字典')

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

print(bob['name'], sue['pay'])
print(bob['name'].split()[-1])

sue['pay'] *= 1.10
print(sue['pay'])

print('\n')

# 其他建立字典的方法
print('其他建立字典的方法')
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)
print(sue)

# 一次一个字段的填写字典
sue = {}
sue['name'] = 'Sue Jones'
sue['age']  = 45
sue['pay']  = 40000
sue['job']  = 'hdw'
print(sue)

# 用zip函数将名/值列表链在一起
names   = ['name', 'age', 'pay', 'job']
values  = ['Sue Jones', 45, 40000, 'hdw']
print(list(zip(names, values)))

sue = dict(zip(names, values))
print(sue)

# 通过一个键序列和所有键得的可选初始值来创建字典(便于初始化字典)
fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
print(record)

print('\n')

#字典列表
print('字典列表')
print(bob)
print(sue)

people = [bob, sue]     # 引用列表
for person in people:
    print(person['name'], person['pay'], sep=', ')      # 所有名字和薪水，用逗号隔开

for person in people:
    if person['name']  == 'Sue Jones':
        print(person['pay'])

# 将数据库映射到"name"字段列
names = [person['name'] for person in people]
print(names)

print(list(map((lambda x: x['name']), people)))     # lambda:匿名函数

print(sum(person['pay'] for person in people))

# 类似SQL查询的效果
print([rec['name'] for rec in people if rec['age'] >= 45])
print([(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people])

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())     # 迭代输出

# 使用通用的python语法进行访问和更新
for person in people:
    print(person['name'].split()[-1])

    person['pay'] *= 1.10
for person in people:
    print(person['pay'])

print('\n')

# 嵌套结构
print('嵌套结构')

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},      # 字典、列表和元祖嵌套在另一个字典中
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}

print(bob2['name'])     # 两次索引
print(bob2['name']['last'])
print(bob2['pay'][1])


# 获取和改变嵌套数据
for job in bob2['job']:
    print(job)

print(bob2['job'][-1])
bob2['job'].append('jantior')       # bob得到一个新工作
print(bob2)

print('\n')

# 字典的字典
print('字典的字典')

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)

db = {}     # 引用字典中的字典
db['bob'] = bob
db['sue'] = sue
print(db['bob']['name'])

db['sue']['pay'] = 50000        # 改变sue薪水
print(db['sue']['pay'])

print(db)
import pprint
pprint.pprint(db)       # 美观打印

for key in db:
    print(key, '=>', db[key]['name'])

for key in db:
    print(key, '=>', db[key]['pay'])

for key in db:
    print(db[key]['name'].split()[-1])      # 使用键索引
    db[key]['pay'] *= 1.10

for record in db.values():      # 迭代字典的值集合来直接访问记录
    print(record['pay'])

x = [db[key]['name'] for key in db]
print(x)

x = [rec['name'] for rec in db.values()]
print(x)

db['tom'] = dict(name='Tom', age=50, job=None, pay=0)       # 新增一条记录，把它赋给一个新的键
print(db['tom'])
print(db['tom']['name'])
print(list(db.keys()))
print(len(db))
print([rec['age'] for rec in db.values()])
print([rec['name'] for rec in db.values() if rec['age'] >= 45])