import os


db = {
    'host': '127.0.0.1',
    'user': 'root',
    'port': '3306',
    'password': 'password',
    'db': 'chat'
}


settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    debug=True,
)