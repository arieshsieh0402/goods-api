from psycopg2.extras import RealDictCursor


from db.connection import conn_pool


class LoginDao:
    def __init__(self):
        self.conn = None
        self.cur = None

    def user_auth(self, account, password):
        try:
            self.conn = conn_pool.getconn()
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            self.cur.execute(
                'EXECUTE validate_user(%(account)s, %(password)s)',
                {'account': account, 'password': password}
            )
            result = self.cur.fetchone()

            return result
        except Exception as err:
            raise err
        finally:
            if self.cur:
                self.cur.close()
            if self.conn:
                conn_pool.putconn(conn=self.conn)
