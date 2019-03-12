#Author:命命
#coding=utf-8
import configparser
import codecs

class ReadConfig:
    """
    读取ini配置文件
    """
    def __init__(self, filename):
        # configpath = os.path.join(prjDir,filename)
        configpath = filename
        # print(configpath)
        fd = open(configpath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self, env, name):
        """
        [projectConfig]
        project_path=E:/fengsulian
        :param env:[projectConfig]
        :param name:project_path
        :return:E:/fengsulian
        """
        return self.cf.get(env, name)
