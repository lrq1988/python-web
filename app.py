from route import path
import tornado.web
import os
import torndb
from tornado.options import define, options

define("mysql_host", default="127.0.0.1:3306", help="db host")
define("mysql_database", default="hello", help="db name")
define("mysql_user", default="root", help="db user")
define("mysql_password", default="", help="db password")

db = torndb.Connection(
    host=options.mysql_host,
    database=options.mysql_database,
    user=options.mysql_user,
    password=options.mysql_password
)

SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application(
                handlers = path,
                db = db,
                **SETTINGS
)
