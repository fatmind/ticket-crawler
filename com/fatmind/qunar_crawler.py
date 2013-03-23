
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
    
    #hold all crawler run state
    crawler_list = {}
    crawler_list["Test"] = 0
    
    #send mail
    mail_sender = mail_sender.MailSender()

    _url = "http://ws.qunar.com/holidayService.jcp?lane="
    interval_time = 5
    from_ = None
    to_ = None 
    date = None
    discount = None
    mail_revicer = None


    def __str__(self):
        return self.from_ + "-" + self.to_ + ", " + self.date + ", " + self.discount + ", " + self.mail_revicer
    

    def __init__(self, from_, to_, date, discount, mail_revicer):
        super(QunarCrawler, self).__init__()
        self.from_ = from_
        self.to_ = to_
        self.date = date
        self.discount = discount
        self.mail_revicer = mail_revicer
    
           
    def run(self):
        QunarCrawler.crawler_list[self] = 0
        try :
            while True :
                sub = self.from_ + "-" + self.to_
                req_res = urllib2.urlopen(urllib2.Request(self._url + sub))
                QunarCrawler.log.info(self.__str__() + " - " + str(req_res.code) + " - " + req_res.msg)
                root = xmlTree.parse(req_res).getroot()
                lines = root.find("airline") 
                for e in lines :
                    if e.attrib["date"] == self.date :
                        for c in e :
                            if c.attrib["type"] == "go" and float(c.attrib["discount"][:-1]) < float(self.discount):
                                msg = c.attrib["price"] + " ~ "  + c.attrib["discount"]
                                QunarCrawler.log.info(self.__str__() + " : " + msg)
                                self.mail_sender.send_mail(self.mail_revicer, sub, msg)
                                QunarCrawler.crawler_list[self] = 1
                                return
                time.sleep(self.interval_time)
        except Exception, e:
            self.log.error(e)
            print traceback.format_exc()
                        

if __name__ == "__main__" :
    interval_time = 2
    qunar_crawler = QunarCrawler("上海", "长春", "2013-04-01", 4.5, "shijianwu1986@163.com")
    qunar_crawler.start()
    print "qunar crawler starting ..."        
        
    