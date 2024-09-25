"""
数据定义的类
"""
class Record:
    def __init__(self,date,id,money,province):
        self.date = date
        self.id = id
        self.money = money
        self.province = province
    # 将文件中内容传给Record类对象，并封装在list[Record]中返回，在外部用定义的列表承接后打印
    # 只会输出Record类对象中成员变量的内存地址
    def __str__(self):
        return f'{self.date},{self.id}: {self.money} {self.province}'
    # 通过__str__魔术方法改变想要返回的数据模式：返回具体的成员变量