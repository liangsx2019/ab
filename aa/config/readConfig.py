# _*_ coding:utf-8 _*_
import os,codecs
import configparser

get_path = os.path.dirname(os.path.abspath('.'))
path = get_path+"//config//"#调用实例化
#print(path)
#config_path = os.path.join(path, 'config.ini')# 方法一
config_path= path+"config.ini" #方法二

config = configparser.ConfigParser()#调用外部的读取配置文件的方法
#config.read(config_path,encoding="utf-8-sig")#utf-8,python3 是utf-8-sig

config.read(config_path,encoding="utf-8-sig")
#config.readfp(codecs.open(config_path, "r", "utf-8-sig"))


class ReadConfig():

	def get_email(self, name):
		value = config.get("EMAIL", name)

	"""
	def get_http(self, name):
		value = config.get('HTTP', name)
		return value

		return value
	def get_mysql(self, name):#写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
		value = config.get('DATABASE', name)
		return value


	"""

if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
   #print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
   print('EMAIL中的开关on_off值为：', ReadConfig().get_email("on_off"))
