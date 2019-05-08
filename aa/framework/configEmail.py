import os
import win32com.client as win32
from config.globalparameter import test_case_path,report_name,report_path
import datetime
import sys
sys.path.append('../')
from config import readConfig
#import getpathInfo



read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')#从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))#从配置文件中读取，邮件类型
addressee = read_conf.get_email('addressee')#从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')#从配置文件中读取，邮件抄送人
#mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
mail_path =report_path
report_path=report_path.replace('\\','\\\\')
print(report_path+'201905051611Report.html')

class send_email():
	def outlook(self):
		app= 'Outlook'
		#olook = win32.Dispatch("%s.Application" %app)
		olook = win32.gencache.EnsureDispatch("%s.Application" % app)
		mail = olook.CreateItem(win32.constants.olMailItem)
		mail.To = addressee # 收件人
		mail.CC = cc # 抄送
		mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject#邮件主题
		#mail.Attachments.Add(mail_path, 1, 1, "myFile")
		#print(mail_path)
		#mail_path1=mail_path.replace('\\','\\\\')
		#print("1",mail_path1)
		#mail.Attachments.Add(report_path,1,1,'*.Report.html') # 通过
		mail.Attachments.Add(report_path+'201905051611Report.html')  # 调试不通过

		#mail.Attachments.Add(mail_path1) #调试不通过
		
		content = """
					报告已发送！
				"""
		mail.Body = content
		mail.Send()


if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
	print(subject)
	send_email().outlook()
	print("send email ok!!!!!!!!!!")
