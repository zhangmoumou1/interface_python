# interface-python
注意事项：<br>
<br>
运行此项目前，先修改[config.ini](https://github.com/zhangmoumou1/interface_python/blob/master/config/config.ini)的路径，此路径为项目本地路径；此接口数据为字典格式，用到实际项目中请转换成json、xml或其他格式<br>
## 一、实现方法<br>
1.通过python+flask编写Restful API，方便调试此框架<br>
<br>
2.运行Restful_Api下的[resfulapi.py](https://github.com/zhangmoumou1/interface_python/blob/master/Restful_Api/resfulapi.py)，可先通过postman或其他接口工具自测接口是否运行正常，停止运行可结束进程，<br>
具体请求结果可查看博客http://www.zhangyanc.club/blog/82<br>
<br>
3.使用python的requests模块请求接口，官方文档http://docs.python-requests.org/zh_CN/latest/user/quickstart.html<br>
<br>
4.这里使用ddt数据驱动读取Excel中的测试用例执行<br>
<br>
5.输出测试报告和日志<br>

## 二、框架目录的讲解<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/%E6%9E%B6%E6%9E%84%E5%9B%BE.jpg)<br>
<br>
1.Public和branch文件夹主要写一些公共、处理方法,如请求的二次封装、获取Excel数据、日志输出、测试报告优化,配置文件读取等;<br>
<br>
2.Restful_Api文件夹为接口的实现，运行[resfulapi.py](https://github.com/zhangmoumou1/interface_python/blob/master/Restful_Api/resfulapi.py),通过postman请求验证;<br>
<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/postman.jpg)<br>
<br>
3.config文件夹用例管理路径,[config.ini](https://github.com/zhangmoumou1/interface_python/blob/master/config/config.ini)为项目的主路径,[globalparam.py](https://github.com/zhangmoumou1/interface_python/blob/master/config/globalparam.py)为日志文件、测试用例读取和存储的路径;<br>
<br>
4.report文件夹下存放日志和测试报告;<br>
<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.jpg)<br>
<br>
![no view](https://github.com/zhangmoumou1/interface_python/blob/master/readme/%E6%97%A5%E5%BF%97.jpg)<br>
<br>
5.testCase文件夹写了测试用例,通过ddt数据驱动读取Excel文件,用unittest单元测试框架管理用例;<br>
<br>
6.testdata文件下是测试用例;<br>
<br>
7.运行[run_ddt_case.py](https://github.com/zhangmoumou1/interface_python/blob/master/run_ddt_case.py)执行用例(如果整个调用流程不太懂的可以看readme下的xmind流程图)。<br>

## 三、更新优化中. . .
### 2018.11.02---更新flask接口代码，用例增加post、put、delete请求方式<br>
1.在此之前只有单一的get接口请求，完善其他几种请求方式<br>
2.用例中包括请求成功和失败的案例<br>
### 2018.11.04---优化支持多断言，可对resultcode、指定返回字段进行断言<br>
实现逻辑：<br>
1.Excel中新增"期望2"列，提供断言期望值<br>
2.请求响应字段为字典格式，指定字段断言，前提需从Excel期望值中获取key值，来指定返回请求的value值<br>
3.如接口只对resultcode断言，对Excel“期望2”列参数为"param=null"作为判断依据，详见[ddt_case.py](https://github.com/zhangmoumou1/interface_python/blob/master/testCase/ddt_case.py)代码<br>
4.新增多个断言需修改代码<br>
### 2018.11.05---增加mysql、oracle、SQLserver数据库的操作<br>
实现逻辑：<br>
1.新增[readyaml.py](https://github.com/zhangmoumou1/interface_python/blob/master/config/readyaml.py)、[db.yaml](https://github.com/zhangmoumou1/interface_python/blob/master/config/db.yaml)、[operate_db.py](https://github.com/zhangmoumou1/interface_python/blob/master/Public/operate_db.py)<br>
1.使用yaml文件管理数据库连接信息（此为个人服务器的数据库请不要随意改动数据）<br>
2.通过接口url和数据库名关联，来判断执行接口需操作对应库<br>
3.通过接口url和SQL语句关联，来判断执行接口所要执行的SQL<br>
4.在[select_request.py](https://github.com/zhangmoumou1/interface_python/blob/master/Public/select_request.py)中进行数据库操作获取请求数据<br>
### 2018.11.07---测试报告用例名的优化和界面美化<br>
1.使用现有的ddt数据驱动不能体现具体用例名称，修改ddt源码从Excel中传入用例名，参考https://www.cnblogs.com/Simple-Small/p/9230382.html<br>
2.在以往测试报告上增加通过百分比和其他优化<br>
### 2018.12.07---支持读取多个Excel文件<br>
实现逻辑：<br>
1.在实际工作中测试用例不可能只写在一个Excel中，支持读取多个<br>
2.更改[get_excel.py](https://github.com/zhangmoumou1/interface_python/blob/master/Public/get_excel.py)，从指定文件夹下获取Excel文件，读取所有用例存到列表里<br>
3.注意Excel文件的命名，以实际代码处理为准<br>
<br>
<br>

## 有问题QQ：1392364470，觉得不错的Fork一下我哦!