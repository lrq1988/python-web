__author__ = 'leefelix'

import tornado.web
import app

class UserHandler(tornado.web.RequestHandler):
    def get(self, method):
        if method == "toadd":
            self.render("useradd.html")
        elif method == "toedit":
            id = self.get_argument('id')
            user = app.db.query("select * from users where id=%s", id)[0]
            print(user)
            self.render("useredit.html", user = user)
        else:
            users = app.db.query("select * from users")
            count = len(users)
            self.render('userlist.html', users=users ,count=count)

    def post(self, method):
        users = app.db.query("select * from users")
        count = len(users)
        self.render('userlist.html', users=users ,count=count)

class UseraddHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        id = self.get_argument('id')
        uname = self.get_argument('uname')
        app.db.execute("insert into users values(%s,%s)", id, uname)
        self.write("{\"statusCode\":\"200\","
                   " \"message\":\"add success\","
                   " \"callbackType\":\"closeCurrent\"}")
        self.finish()

class UsereditHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        id = self.get_argument('id')
        uname = self.get_argument('uname')
        app.db.execute("update users set uname=%s where id=%s", uname, id)
        self.write("{\"statusCode\":\"200\","
                   " \"message\":\"edit success\","
                   " \"callbackType\":\"closeCurrent\"}")
        self.finish()

class UserdelHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        id = self.get_argument('id')
        print(id)
        app.db.execute("delete from users where id=%s", id)
        self.write("{\"statusCode\":\"200\","
                   " \"message\":\"deleted\","
                   " \"callbackType\":\"closeCurrent\"}")
        self.finish()
