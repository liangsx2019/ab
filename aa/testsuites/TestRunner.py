import unittest
import time,sys,os,codecs
import HTMLTestRunner
#报告文件路径
report_path=os.path.dirname(os.path.abspath('.'))+'\\reports\\'
#system time
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#report file
Htmlfile=report_path+now+"htmlreport.html"
fp=codecs.open(Htmlfile,'a','utf-8')
#构建suite
suite=unittest.TestLoader().discover("testsuites")

if __name__=="__main__":
    print(Htmlfile)
    #初始化HTMLTestRunner实例对象，生产报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"AAA项目测试报告",description=u"用例测试情况")
    #开始执行测试套件
    runner.run(suite)

