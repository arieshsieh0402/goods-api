INSERT INTO system_user (account, password)
VALUES ('account_1', crypt('password_1', gen_salt('bf')));


INSERT INTO goods (name)
VALUES
    ('商品名稱_1'),
    ('商品名稱_2');
