from Data.read_data import Op_data
from time import sleep

def get_data():
    yml_list = []
    data = Op_data('data.yml').read_yaml().get('Login_Data')
    sleep(3)
    for i in data:
        for o in i.keys():
            yml_list.append((o,i.get(o).get('accounts'),
                             i.get(o).get('password'),i.get(o).get('category_1'),i.get(o).get('category_2'),
                             i.get(o).get('dim'),i.get(o).get('tag'),i.get(o).get('quit_succeed'),i.get(o).
                             get('get_quit'),i.get(o).get('close')))

    return yml_list
