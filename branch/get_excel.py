# -*- coding: utf-8 -*-
import os

import xlrd

from branch.log import Log
from config import globalparam

log_path = globalparam.log_path
file_path = globalparam.data_path

def datacel(filrpath):
    try:
        file = xlrd.open_workbook(filrpath)
        me = file.sheets()[0]
        nrows = me.nrows
        listid = []
        listname = []
        listkey = []
        listconeent = []
        listparam_place = []
        listurl = []
        listfangshi = []
        listqiwang1 = []
        listqiwang2 = []
        for i in range(1, nrows):
            listid.append(me.cell(i, 0).value)
            listname.append(me.cell(i, 1).value)
            listkey.append(me.cell(i, 2).value)
            listconeent.append(me.cell(i, 3).value)
            listparam_place.append(me.cell(i, 4).value)
            listurl.append(me.cell(i, 5).value)
            listfangshi.append((me.cell(i, 6).value))
            listqiwang1.append((me.cell(i, 7).value))
            listqiwang2.append((me.cell(i, 8).value))
        return listid, listname, listkey, listconeent, listparam_place, listurl, listfangshi, listqiwang1, listname, listqiwang2
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

def data(aa):
    path = file_path + "/" + "case{0}.xlsx".format(aa)
    listid, listname, listkey, listconeent, listparam_place, listurl, listfangshi, listqiwang1, listname, listqiwang2=datacel(path)
    make_data1 = []
    try:
        for i in range(len(listid)):
            make_data1.append({'url': listurl[i], 'listname': listname[i],  'key': listkey[i], 'coneent':listconeent[i], 'param_place': listparam_place[i],
                              'fangshi': listfangshi[i], 'expect1': listqiwang1[i], 'expect2': listqiwang2[i]})
            i += 1
        return make_data1
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

def makedata():
    # 获取文件下文件个数
    count = 0
    make_data = []
    for root, dirs, files in os.walk(file_path):
        for each in files:
            count += 1
        print(count)
    #用例整合
    for aa in range(count):
        aa += 1
        for bb in data(aa):
            make_data.append(bb)
    return make_data
