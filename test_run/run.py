import smtplib
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)
from email.mime.multipart import MIMEMultipart
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header

test_dir = 'F:\\Auto_app\\test_case'

discovery = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

# 获取最新报告
def new_file(report_dir):

    # 获取列表文件，以列表形式返回
    lists = os.listdir(report_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    file = os.path.join(report_dir, lists[-1])
    return file

#发送邮件方法
def send_mail(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    #读取文件内容
    mail_body = f.read()
    f.close()
    #邮件服务器内容
    smtpserver = 'smtp.qq.com'
    user = '724253911@qq.com'
    password = 'hrdfkupqxsambdgf'
    sender = '724253911@qq.com'
    receivers = ['867773842@qq.com', 'chenyaojie@homeking365.com']
    subject = '测试报告'

    #报告正文

    # text="Dear all!\n附件是最新测试报告。\n麻烦下载下来观看，用户火狐浏览器打开。\n请知悉，谢谢！"
    # msg_plain=MIMEText(text,'plain','utf-8')
    # msg.attach(msg_plain)


    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)
    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    print('开始发送邮件')
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print('邮件发送结束')


if __name__ == '__main__':
    report_dir = 'F:\\Auto_app\\test_result\\report'
    now = time.strftime('%Y-%m-%d-%H_%M_%S')
    report_name = report_dir + '/' + now + 'report.html'

    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='测试报告', description='测试结果')

        runner.run(discovery)
    f.close()

    new_report = new_file(report_dir)
    send_mail(new_report)

