#Author:命命
import requests
import time
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
import xml.etree.ElementTree as ET

class Interface_xml():
    """
    csu接口断言
    """
    def __init__(self):
        self.tag = 'Request'
        self.d = {"accountId": "445511", "timeStamp": "2018-05-22 03:16:58", "accessToken": "1", "authString": "1", "portalType": "13"}

    def dict_to_xml(self):
        elem = Element(self.tag)
        for key, val in self.d.items():
            child = Element(key)
            child.text = str(val)
            elem.append(child)
        return elem



    def xml_to_dic(self):
        msg = {}
        root_elem = ET.fromstring(self.test_yunda())
        for ch in root_elem:
                msg[ch.tag] = ch.text
        return msg


data = Interface_xml()
print(data.xml_to_dic())


