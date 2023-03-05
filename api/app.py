from flask import Flask
from flask_restful import Api

from common.config import config_server, config_auth
from resources.add_good import AddGoods
from resources.good import Good
from resources.goods import Goods
from resources.login import Login


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = config_auth['secret_key']
api_port = 5000


api.add_resource(Login, '/auth/login')
api.add_resource(Goods, '/goods')
api.add_resource(Good, '/goods/<string:uuid>')
api.add_resource(AddGoods, '/goods/add')


app.run(port=config_server['port'])
