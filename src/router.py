import tornado.web
import tornado.ioloop
from handler.admin.admin_handler import LoginHadler, RegistHandler, UpdatePwdHandler, DeleteUserHandler

settings = {
    'template_path': 'template',
}


application = tornado.web.Application({
    (r"/login", LoginHadler),
    (r"/regist", RegistHandler),
    (r"/updatepwd", UpdatePwdHandler),
    (r"/delete", DeleteUserHandler)
}, **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()