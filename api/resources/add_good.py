from flask import make_response, request
from flask_restful import Resource

from common.auth import jwt_required
from common.exceptions import InvalidTokenError, ExpiredTokenError
from db.goods_dao import GoodsDao


class AddGoods(Resource):
    def post(self):
        try:
            jwt_required()
            raw_data = request.get_json()
            name = raw_data['goods_name']
            dao = GoodsDao()
            id_dict = dao.add_good(name)
            good_id = id_dict['_id']
            result = dao.get_good_by_id(good_id)
            return make_response(result, 200)
        except ExpiredTokenError:
            return make_response('權限錯誤', 403)
        except InvalidTokenError:
            return make_response('權限錯誤', 403)
        except Exception:
            return make_response('系統錯誤', 500)
