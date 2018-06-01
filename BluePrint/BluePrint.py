from flask import Flask

app = Flask(__name__)

# 3----注册蓝图对象给程序实例
from qwe.Person import api
app.register_blueprint(api)

from shop_goods.shop import shop
app.register_blueprint(shop, url_prefix = "/shop")

@app.route('/')
def index():
    return 'index'

@app.route('/home')
def home():
    return 'Hello home!'

@app.route('/detail')
def detail():
    return 'Hello detail!'

@app.route('/list')
def list():
    return 'Hello list!'

@app.route("/github")
def github():
    return "github"

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True ,port=5556)
