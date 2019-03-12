# -*- coding: utf-8 -*-
import os, xlrd
from Branch.log import Log
from config import globalparam

log_path = globalparam.log_path
file_path = globalparam.data_path

def readexcel(filepath):
    """
    读取xlsx文件，将每列的数据保存到list里
    """
    try:
        file = xlrd.open_workbook(filepath)
        first_line = file.sheets()[0]
        lines = first_line.nrows
        list_id = []
        list_name = []
        list_key = []
        list_param = []
        list_place = []
        list_url = []
        list_way = []
        list_expect1 = []
        list_expect2 = []
        for i in range(1, lines):
            list_id.append(first_line.cell(i, 0).value)
            list_name.append(first_line.cell(i, 1).value)
            list_key.append(first_line.cell(i, 2).value)
            list_param.append(first_line.cell(i, 3).value)
            list_place.append(first_line.cell(i, 4).value)
            list_url.append(first_line.cell(i, 5).value)
            list_way.append((first_line.cell(i, 6).value))
            list_expect1.append((first_line.cell(i, 7).value))
            list_expect2.append((first_line.cell(i, 8).value))
        return list_id, list_name, list_key, list_param, list_place, list_url, list_way, list_expect1, list_expect2
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

def data(aa):
    path = file_path + "/" + "case{0}.xlsx".format(aa)
    list_id, list_name, list_key, list_param, list_place, list_url, list_way, list_expect1, list_expect2=readexcel(path)
    make_data1 = []
    try:
        for i in range(len(list_id)):
            make_data1.append({'id': list_id[i], 'url': list_url[i], 'name': list_name[i],  'key': list_key[i], 'param':list_param[i], 'place': list_place[i],
                              'way': list_way[i], 'expect1': list_expect1[i], 'expect2': list_expect2[i]})
            i += 1
        return make_data1
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

def mergedata():
    # 获取文件下文件个数
    count = 0
    make_data = []
    for root, dirs, files in os.walk(file_path):
        for each in files:
            count += 1
        print(count)
    #用例整合
    for case in range(count):
        case += 1
        for i in data(case):
            make_data.append(i)
    return make_data
