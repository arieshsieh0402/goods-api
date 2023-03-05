from flask import make_response
from flask_restful import Resource

from common.auth import jwt_required
from common.exceptions import InvalidTokenError, ExpiredTokenError
from db.goods_dao import GoodsDao


class Goods(Resource):
    def get(self):
        try:
            jwt_required()
            dao = GoodsDao()
            result = dao.get_goods()
            return make_response(result, 200)
        except ExpiredTokenError:
            return make_response('權限錯誤', 403)
        except InvalidTokenError:
            return make_response('權限錯誤', 403)
        except Exception:
            return make_response('系統錯誤', 500)
