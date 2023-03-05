-- Create pgcrypto extension
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create table of system user
DROP TABLE IF EXISTS system_user CASCADE;

CREATE TABLE system_user (
  _id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  account VARCHAR(128) UNIQUE NOT NULL,
  password VARCHAR(128) NOT NULL
);


-- Create table of goods
DROP TABLE IF EXISTS goods CASCADE;

CREATE TABLE goods (
  _id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  name VARCHAR(128) NOT NULL
);
