# -*- coding: utf-8 -*-
import xlrd
from Public.log import Log
from config import globalparam

log_path = globalparam.log_path

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

def makedata():
    #import os
    #path = os.getcwd() + '\\test_case_data\\case.xlsx'
    #path = globalparam.data_path + "\\" + "case.xlsx"
	path = globalparam.data_path + "/" + "case.xlsx"
    listid, listname, listkey, listconeent, listparam_place, listurl, listfangshi, listqiwang1, listname, listqiwang2=datacel(path)
    make_data = []
    try:
        for i in range(len(listid)):
            make_data.append({'url': listurl[i], 'listname': listname[i],  'key': listkey[i], 'coneent':listconeent[i], 'param_place': listparam_place[i],
                              'fangshi': listfangshi[i], 'expect1': listqiwang1[i], 'expect2': listqiwang2[i]})
            i += 1
        return make_data
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)
