import psycopg2
from credentials import db_credentials


class MySQLDataService:
    def __init__(self):
        self.rds_endpoint = db_credentials['rds_endpoint']
        self.db_name = db_credentials['db_name']
        self.db_user = db_credentials['db_user']
        self.db_password = db_credentials['db_password']
        self.conn_string = f"dbname={self.db_name} " \
                           f"user={self.db_user} " \
                           f"password={self.db_password} " \
                           f"host={self.rds_endpoint}"
        self.conn, self.cursor = None, None

    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(self.conn_string)
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print("Unable to connect to the database.")
            print(e)

    def close_connection(self, conn, cursor):
        if cursor:
            self.cursor.close()
        if conn:
            self.conn.close()
        self.conn, self.cursor = None, None

    def read_single_record(self, query):
        result = None
        self.connect_to_db()
        try:
            self.cursor.execute(query=query)
            result = self.cursor.fetchall()
            if len(result) > 1:
                raise Exception("duplicate email")
        except psycopg2.Error as e:
            print("read single record failed.")
            print(e)
        finally:
            self.close_connection()
            return result

    def insert_single_record(self, query):
        self.connect_to_db()
        try:
            self.cursor.execute(query=query)
        except psycopg2.Error as e:
            print("insert single record failed.")
            print(e)
        finally:
            self.close_connection()