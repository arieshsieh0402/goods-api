from flask import make_response, request
from flask_restful import Resource

from common.auth import generate_token
from db.login_dao import LoginDao


class Login(Resource):
    def post(self):
        try:
            dao = LoginDao()
            data = request.get_json()
            account, password = data['account'], data['password']
            result = dao.user_auth(account, password)

            if result:
                token = generate_token(account)
                response = make_response(
                    {'account': data['account'], 'name': '使用者名稱'}, 200
                )
                response.headers['Authorization'] = token
                return response
            else:
                return make_response('帳號密碼錯誤', 401)
        except Exception:
            return make_response('系統錯誤', 500)
