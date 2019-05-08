#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
description:APP执行测试
'''
import unittest,time,HTMLTestRunner,codecs
from config.globalparameter import test_case_path,report_name
#from framework import send_mail


# 构建测试集,包含testsuites目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test*.py')
#解释test_case_path = project_path+"\\testsuites\\"

# 执行测试
if __name__=="__main__":
	report = report_name+"Report.html"
	fb = open(report,'a')
	#fb=codecs.open(report,'a','utf-8')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fb,
		title=u'88APP自动化测试报告',
		description=u'项目描述：生产环境'
	)
	runner.run(suite)
	fb.close()
	"""
	# 发送邮件
	time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
	email = send_mail.send_email()
	email.sendReport()
	"""