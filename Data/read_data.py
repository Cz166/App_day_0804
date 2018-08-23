import os,yaml


class Op_data:

    def __init__(self,file_name):
        self.file_path = os.getcwd() + os.sep + 'Data' + os.sep + file_name
    # 读yaml文件
    def read_yaml(self):
        with open(self.file_path,'r',encoding='utf-8') as f:
            return yaml.load(f)
    # 写yaml文件
    def write_yaml(self,data):
        with open(self.file_path,'w',encoding='utf-8') as h:
            return yaml.dump(data,h)



