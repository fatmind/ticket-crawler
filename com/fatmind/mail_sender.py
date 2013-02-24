#coding=utf-8

'''
Created on 2013-1-27

@author: bohan.sj
'''

import smtplib
from email.mime.text import MIMEText


class MailSender():
    '''
    send mail util
    '''
    mail_host = "smtp.163.com"
    mail_user = "shijianwu1986"
    mail_pass = "5shijianMa"
    mail_postfix = "163.com"
      
    def send_mail(self, dest_list, sub, content): 
        
        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEText(content, _charset="utf-8")
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = dest_list
        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host)
            s.login(self.mail_user, self.mail_pass)
            s.sendmail(me, dest_list, msg.as_string())
            s.close()
            return True
        except Exception, e:
            print e
            return False




if __name__ == "__main__" :
    
    mail_sender = MailSender()
    if mail_sender.send_mail("m.shijianwu@gmail.com", "python mail test", "python mail test") :
        print "send mail success"
    else :
        print "send mail fail"
  
