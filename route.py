#coding:utf-8

from handlers.index import MainHandler
from handlers.user import UserHandler, UseraddHandler, UsereditHandler, UserdelHandler

path = [
    (r'/', MainHandler),
    (r'/user/([a-z]*)',UserHandler),
    (r'/useradd', UseraddHandler),
    (r'/useredit', UsereditHandler),
    (r'/userdel', UserdelHandler)

]


