from email.mime.text import MIMEText
import smtplib
from Util.common_util import CommonUtil
class SendEmail:
    global send_user_qiye, send_user_qq
    global email_host_qiye, email_host_qq
    global password_qiye, password_qq

    email_host_qiye = 'smtp.qiye.163.com'
    send_user_qiye = 'jiyanjiao@aerozhonghuan.com'
    password_qiye = 'Zhonghuan2019010'

    email_host_qq = 'smtp.qq.com'
    send_user_qq = '771469575@qq.com'
    password_qq = 'myplhvsquinfbefc'#此处使用授权码

    """使用企业163邮箱发送邮件"""
    def send_mail_qiye(self,user_list,sub,content):
        user = "jiyanjiao"+"<"+send_user_qiye+">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host_qiye)
        server.login(send_user_qiye,password_qiye)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    """使用qq邮箱发送邮件"""
    def send_mail_qq(self,user_list,sub,content):
        user = "jiyanjiao" + "<" + send_user_qq + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP_SSL(email_host_qq,465)
        server.login(send_user_qq, password_qq)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    """发送带html的测试报告"""
    def send_email_html(self,user_list,sub):
        user = "jiyanjiao" + "<" + send_user_qiye + ">"
        cu = CommonUtil()
        file = cu.find_report_file()
        f = open(file, 'rb')
        mail_body = f.read()
        f.close()
        message = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host_qiye)
        server.login(send_user_qiye, password_qiye)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    """发送测试报告"""
    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        pass_result = "%.2f%%"%(pass_num/count_num*100)
        fail_result = "%.2f%%"%(fail_num/count_num*100)

        user_list = ['771469575@qq.com']
        sub = "慕课版接口测试报告"
        content = "此次一共运行接口个数为%s个,通过个数为%s个.失败个数为%s,通过率为%s"%(count_num,pass_num,fail_num,pass_result)
        self.send_mail_qq(user_list,sub,content)


if __name__ == '__main__':
    s = SendEmail()
    user_list = ['jiyanjiao@aerozhonghuan.com','771469575@qq.com']
    #s.send_mail_qiye(user_list,"企业测试邮件","hi,everyone")
    #s.send_mail_qq(user_list,"qq测试邮件","hi,everyone")
    #s.send_main([1],[1])
    s.send_email_html(user_list,'html测试邮件')
