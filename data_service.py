import psycopg2
from credentials import db_credentials

rds_endpoint = db_credentials['rds_endpoint']
db_name = db_credentials['db_name']
db_user = db_credentials['db_user']
db_password = db_credentials['db_password']
conn_string = f"dbname={db_name} user={db_user} password={db_password} host={rds_endpoint}"

def connect_to_db():
    try:
        connection = psycopg2.connect(conn_string)
        cursor = connection.cursor()
        return cursor
    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)

if __name__ == "__main":
    cursor = connect_to_db()
