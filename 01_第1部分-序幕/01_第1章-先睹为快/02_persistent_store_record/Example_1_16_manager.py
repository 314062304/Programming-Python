#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

"""         增加继承        """

# 定制person.py中的Person类，以便涨薪时缺省为经理额外增加10%的奖金

from Example_1_15_person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


# class Manager(Person):
#     def giveRaise(self, percent, bonus=0.1):
#         Person.giveRaise(self, percent + bonus)       # 通过增强继承来实现


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastname())
    tom.giveRaise(.20)
    print(tom.pay)