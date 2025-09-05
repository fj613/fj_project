# 读取TXT文档数据

def get_txt_data():
    with open(r'C:\Users\syb\python_fj\pythonProject_fj\pythonProject_fj\data\login_data.txt',
              encoding='utf-8') as file:
        contents = file.readlines()
        list_data1 = []
        list_data2 = []
        for i in contents:
            list_data1.append(i.strip())
        else:
            for i in list_data1:
                list_data2.append(i.split(','))
        # print(list_data2)
        return list_data2


# login_datas = get_txt_data()
# for i in login_datas:
#     print(i[0])
#     print(i[1])

# print(get_txt_data())
