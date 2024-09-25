"""
文件定义的类对象
"""
import json

from data_define import Record


# 定义一个抽象类，再通过子类完成数据的读取
class Filereader:
    def read_file(self)->list[Record]:
        # 读取文件，读到的每一条数据都作为Record类对象，并封装到list列表中
        pass

# 定义一个子类完成txt文本的读取
class Textfileread(Filereader):
    def __init__(self,path):
        self.path = path
# 定义接收文件路径的成员变量
    def read_file(self) -> list[Record]:
        f = open(self.path,"r",encoding="utf-8")
        record_list:list[Record] = []
        for line in f.readlines():
            # print(line)
            line = line.strip()
            line_list = line.split(",")
            record = Record(line_list[0],line_list[1],int(line_list[2]),line_list[3])
            record_list.append(record)

        f.close()
        return record_list

class Jsonfileread(Filereader):
    def __init__(self,path):
        self.path = path
    def read_file(self) -> list[Record]:
        f = open(self.path,"r",encoding="utf-8")
        record_list:list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            # print(data_dict)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list



if __name__ == '__main__':
    text_file_reader = Textfileread("D:/2011年1月销售数据.txt")
    json_file_reader = Jsonfileread("D:/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_file()
    list2 = json_file_reader.read_file()
# 读取后的数据以列表的形式封装
    for l in list1:
        print(l)
    for l in list2:
        print(l)









