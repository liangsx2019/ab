1 # coding:utf-8

'''
description:配置全局参数
'''
import time,os

# 获取项目路径
project_path=os.path.dirname(os.path.abspath('.'))

# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path+"\\testsuites\\"
# print 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path+"\\reports\\"
report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())
"""
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正,#smtp.exmail.qq.com
email_name = "1961603670@qq.com"  # 发件人名称
email_password = "xxxxxx"  # 发件人登录密码
email_To = 'weshangheguoji@qq.com;liangshixin@fang.com;2393799390@qq.com'  # 收件人
"""