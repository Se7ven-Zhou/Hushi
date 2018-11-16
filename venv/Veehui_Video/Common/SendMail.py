# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg_from = '406574570@qq.com'  # 发送方邮箱
passwd = 'regbjpmjbqgocbdg'  # 填入发送方邮箱的授权码
msg_to = '406574570@qq.com'  # 收件人邮箱

title = "python邮件测试"  # 主题
content = "xxx"
# 正文
msg = MIMEText(content,_subtype='html',_charset='utf-8')
msg['Subject'] = title
msg['From'] = msg_from
msg['To'] = msg_to
try:
    # 邮件服务器及端口号
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")
except s.SMTPException as e:
    print("发送失败")
finally:
    s.quit()
