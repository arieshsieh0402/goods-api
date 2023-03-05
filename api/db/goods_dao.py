from psycopg2.extras import RealDictCursor

from db.connection import conn_pool


class GoodsDao:
    def __init__(self):
        self.conn = None
        self.cur = None

    def execute_query(
        self,
        query: str,
        param: dict = None,
        commit: bool = False,
        fetch_type: str = None
    ):
        try:
            self.conn = conn_pool.getconn()
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

            if query and param:
                self.cur.execute(query, param)
            else:
                self.cur.execute(query)

            fetch_methods = {
                'all': self.cur.fetchall,
                'one': self.cur.fetchone
            }

            if commit:
                self.conn.commit()
            if fetch_type in fetch_methods:
                result = fetch_methods[fetch_type]()
                return result
        except Exception as err:
            raise err
        finally:
            if self.cur:
                self.cur.close()
            if self.conn:
                conn_pool.putconn(conn=self.conn)

    def get_goods(self):
        query = 'EXECUTE get_goods'

        return self.execute_query(query, fetch_type='all')

    def get_good_by_id(self, uuid):
        query = 'EXECUTE get_good_by_id(%(uuid)s)'
        param = {'uuid': uuid}

        return self.execute_query(query, param, fetch_type='one')

    def add_good(self, name):
        query = 'EXECUTE add_good(%(name)s)'
        param = {'name': name}

        return self.execute_query(query, param, commit=True, fetch_type='one')

    def put_good(self, uuid, name):
        query = 'EXECUTE put_good(%(uuid)s, %(name)s)'
        param = {'uuid': uuid, 'name': name}

        return self.execute_query(query, param, commit=True)

    def delete_good(self, uuid):
        query = 'EXECUTE delete_good(%(uuid)s)'
        param = {'uuid': uuid}

        return self.execute_query(query, param, commit=True)
