#coding:utf-8

import tornado.web
import app


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index_menu.html')



