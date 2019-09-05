#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

"""         添加行为        """

# 将获取姓名和增加薪水的逻辑添加为类的方法，方法使用self参数来访问或更新被处理的实例（记录）

class Person:
    def __init__(self,  name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastname(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)

    print(bob.lastname())
    sue.giveRaise(.10)
    print(sue.pay)