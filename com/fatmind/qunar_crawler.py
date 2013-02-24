
#coding=utf-8

'''
Created on 2013-1-27

@author: bohan.sj
'''

from threading import Thread
import urllib2
from exceptions import Exception
import time
import xml.etree.ElementTree as xmlTree
import mail_sender
import logger_factory
import traceback

class QunarCrawler(Thread):
    '''
    crawler qunar ticket info
    '''
    
    log = logger_factory.LoggerFatory().getLogger("QunarCrawler")

    _url = "http://ws.qunar.com/holidayService.jcp?lane="
    from_ = None
    to_ = None 
    expect_date = None
    expect_discount = None
    interval_time = 5
    mail_revicer = None
    
    mail_sender = mail_sender.MailSender()
    
    state = 0

    def __init__(self, from_, to_, expect_date, expect_discount, mail_revicer):
        super(QunarCrawler, self).__init__()
        self.from_ = from_
        self.to_ = to_
        self.expect_date = expect_date
        self.expect_discount = expect_discount
        self.mail_revicer = mail_revicer
        
    def run(self):
        res_file = open("qunar_res.txt", "w")
        try :
            while True :
                sub = self.from_ + "-" + self.to_
                req_res = urllib2.urlopen(urllib2.Request(self._url + sub))
                print req_res.code, req_res.msg
                root = xmlTree.parse(req_res).getroot()
                lines = root.find("airline") 
                for e in lines :
                    if e.attrib["date"] == self.expect_date :
                        for c in e :
                            if c.attrib["type"] == "go" and float(c.attrib["discount"][:-1]) < 8:
                                msg = c.attrib["price"] + " ~ "  + c.attrib["discount"]
                                print msg
                                self.mail_sender.send_mail(self.mail_revicer, sub, msg)
                                return
                time.sleep(self.interval_time)
        except Exception, e:
            self.log.error(e)
            print traceback.format_exc()
        finally:
            res_file.close()
                        

if __name__ == "__main__" :
    interval_time = 2
    qunar_crawler = QunarCrawler("上海", "长春", "2013-04-01", 4.5, "shijianwu1986@163.com")
    qunar_crawler.start()
    print "qunar crawler starting ..."        
        
    