#coding=utf-8

'''
Created on 2013-2-22

@author: bohan.sj
'''

import web
import qunar_crawler

urls = (
    '/',    'Index',
    '/add', 'AddCrawler'
)

render = web.template.render('templates/')

#key,value
data_map = []

class Index:
    def GET(self):
        crawler_list = qunar_crawler.QunarCrawler.crawler_list
        return render.index(crawler_list)

class AddCrawler:
    def GET(self):
        return render.add_crawler()
    def POST(self):
        params = web.input()
        crawler = qunar_crawler.QunarCrawler(params["from_"], params["to_"], params["date"], params["discount"], params["mail"])
        crawler.start()
        return web.redirect("/")

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
    
