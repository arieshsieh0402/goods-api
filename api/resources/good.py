from flask import make_response, request
from flask_restful import Resource

from common.auth import jwt_required
from common.exceptions import InvalidTokenError, ExpiredTokenError
from db.goods_dao import GoodsDao


class Good(Resource):
    def get(self, uuid):
        try:
            jwt_required()
            dao = GoodsDao()
            result = dao.get_good_by_id(uuid)
            return make_response(result, 200)
        except ExpiredTokenError:
            return make_response('權限錯誤', 403)
        except InvalidTokenError:
            return make_response('權限錯誤', 403)
        except Exception:
            return make_response('系統錯誤', 500)

    def put(self, uuid):
        try:
            jwt_required()
            raw_data = request.get_json()
            name = raw_data['goods_name']
            dao = GoodsDao()
            dao.put_good(uuid, name)
            result = dao.get_good_by_id(uuid)
            return make_response(result, 200)
        except ExpiredTokenError:
            return make_response('權限錯誤', 403)
        except InvalidTokenError:
            return make_response('權限錯誤', 403)
        except Exception:
            return make_response('系統錯誤', 500)

    def delete(self, uuid):
        try:
            jwt_required()
            dao = GoodsDao()
            dao.delete_good(uuid)
            return make_response('成功', 200)
        except ExpiredTokenError:
            return make_response('權限錯誤', 403)
        except InvalidTokenError:
            return make_response('權限錯誤', 403)
        except Exception:
            return make_response('系統錯誤', 500)
