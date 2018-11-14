import tornado.web
import tornado.ioloop
import json
from model import admin


class LoginHadler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):

        username = self.get_argument('username', None)
        password = self.get_argument('pwd', None)
        print(password)
        user = admin.selectUserByUP(username, password)
        if user:
            user_json = json.dumps(user)
            self.write(user_json)
        else:
            self.write('登录失败')


class RegistHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('regist.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        password = self.get_argument('pwd', None)
        user = admin.insertUser(username, password)

        if user:
            self.write('注册成功')
        else:
            self.write('注册失败')

class UpdatePwdHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('updatepwd.html')

    def post(self):
        username = self.get_argument('username', None)
        pasword = self.get_argument('pwd', None)
        result = admin.updatePsw(username, pasword)

        if result:
            self.write('更新成功')
        else:
            self.write('更新失败')


class DeleteUserHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('delete.html')
    def post(self, *args, **kwargs):
        print('0000000')
        username = self.get_argument('username', None)
        print(username)
        result = admin.deleteUserByUsername(username)
        if result:
            self.write('删除成功')
        else:
            self.write('删除失败')