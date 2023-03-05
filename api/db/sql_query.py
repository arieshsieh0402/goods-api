prepare_statements = {
    'validate_user': '''
        PREPARE validate_user(varchar, varchar) AS
        SELECT * FROM system_user
        WHERE account = $1 AND password = crypt($2, password);
    ''',
    'get_goods': '''
        PREPARE get_goods AS
        SELECT * FROM goods;
    ''',
    'get_good_by_id': '''
        PREPARE get_good_by_id(uuid) AS
        SELECT * FROM goods
        WHERE _id = $1;
    ''',
    'add_good': '''
        PREPARE add_good(varchar) AS
        INSERT INTO goods(name)
        VALUES ($1)
        RETURNING _id;
    ''',
    'put_good': '''
        PREPARE put_good(uuid, varchar) AS
        UPDATE goods
        SET name = $2
        WHERE _id = $1;
    ''',
    'delete_good': '''
        PREPARE delete_good(uuid) AS
        DELETE FROM goods
        WHERE _id = $1;
    '''
}
