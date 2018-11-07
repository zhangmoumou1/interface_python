#Author:命命
import requests
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
import xml.etree.ElementTree as ET

class Interface_xml():

    def __init__(self):
        self.tag = 'Request'
        self.d = {"accountId": "445511", "timeStamp": "2018-05-22 03:16:58", "accessToken": "1", "authString": "1", "portalType": "13"}
        # self.tag = 'Request'
        # self.d = {"bookId": "1", "start": "1", "count": "10"}

    def dict_to_xml(self):
        elem = Element(self.tag)
        for key, val in self.d.items():
            child = Element(key)
            child.text = str(val)
            elem.append(child)
        return elem

    def test_yunda(self):
        data2 = self.dict_to_xml()
        data3 = tostring(data2)
        url = 'http://10.211.95.228:9085/csu/portalengine/accessAuthLogin'
        r = requests.post(url,data=data3)
        return r.text

    # def test_yunda(self):
    #     data2 = self.dict_to_xml()
    #     data3 = tostring(data2)
    #     url = 'http://10.211.95.228:9084/cpu/portalengine/getBatchChapterInfos'
    #     r = requests.post(url,data=data3)
    #     return r.text

    def xml_to_dic(self):
        msg = {}
        # root_elem = ET.fromstring(xml_str)
        root_elem = ET.fromstring(self.test_yunda())
        for ch in root_elem:
                msg[ch.tag] = ch.text
        return msg


data = Interface_xml()
print(data.xml_to_dic())


