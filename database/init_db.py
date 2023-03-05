import json

import psycopg2

with open('config.json', 'r') as config_f:
    config = json.load(config_f)
    config = config['database']

conn = psycopg2.connect(
    host=config['host'],
    port=config['port'],
    dbname=config['db_name'],
    user=config['db_username'],
    password=config['db_password']
)

cur = conn.cursor()
with open('reset-db.sql', 'r') as reset_f:
    cur.execute(reset_f.read())
with open('insert-db-dummy-data.sql', 'r') as insert_f:
    cur.execute(insert_f.read())

conn.commit()
cur.close()
conn.close()
