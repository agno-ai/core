CREATE SCHEMA agno_db;

CREATE TABLE agno_db.Account ( 
    account_id INTEGER NOT NULL   AUTO_INCREMENT ,
    account_name VARCHAR( 55 ) NOT NULL    ,
    username VARCHAR( 55 ) NOT NULL    ,
    password_hash VARCHAR( 55 ) NOT NULL    ,
CONSTRAINT PK_Table_0 PRIMARY KEY ( account_id )
 ) ;

CREATE TABLE agno_db.Users ( 
    EntryNo INTEGER NOT NULL   AUTO_INCREMENT ,
    account_id INTEGER NOT NULL    ,
    face_id VARCHAR( 55 ) NOT NULL    ,
    timestamp TIMESTAMP NOT NULL    ,
    emotion VARCHAR( 55 ) NOT NULL    ,
    image BLOB NOT NULL    ,
CONSTRAINT PK_Users PRIMARY KEY ( EntryNo )
 ) ;

CREATE INDEX idx_Users ON agno_db.Users ( account_id );

ALTER TABLE agno_db.Users ADD FOREIGN KEY fk_users_account ( account_id ) REFERENCES agno_db.Account( account_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

