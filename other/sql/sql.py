from sqlalchemy import create_engine
import pymysql

db_connection_str = 'mysql+pymysql://username:password@host/dbname'
db_connection = create_engine(db_connection_str)