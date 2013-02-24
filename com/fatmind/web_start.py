#coding=utf-8

'''
Created on 2013-2-22

@author: bohan.sj
'''

import web
import qunar_crawler
import traceback

urls = (
    '/', 'Index',
    '/start', 'Start'
)

render = web.template.render('templates/')


class Index:
    def GET(self):
        state = qunar_crawler.QunarCrawler.state
        return render.index(state)

class Start:
    
    def GET(self):
        data = self.read_data()
        crawler = qunar_crawler.QunarCrawler("上海", "长春", "2013-04-01", 4.5, "shijianwu1986@163.com")
        crawler.start()
        qunar_crawler.QunarCrawler.state = 1
        return render.index(qunar_crawler.QunarCrawler.state)
    
    def read_data(self):
        try:
            data_file = open("qunar_res.txt", "r")
        except Exception:
            traceback.print_exc()
        finally:
            data_file.close()
            return None
        data = []
        for line in data_file:
            data.append(line)
        return data
            

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()