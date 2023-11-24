import psycopg2
from credentials import db_credentials


class MySQLDataService:
    def __init__(self):
        self.rds_endpoint = db_credentials["rds_endpoint"]
        self.db_name = db_credentials["db_name"]
        self.db_user = db_credentials["db_user"]
        self.db_password = db_credentials["db_password"]
        self.conn_string = (
            f"dbname={self.db_name} "
            f"user={self.db_user} "
            f"password={self.db_password} "
            f"host={self.rds_endpoint}"
        )
        self.conn, self.cursor = None, None

    def open_connection(self):
        try:
            self.conn = psycopg2.connect(self.conn_string)
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print("Unable to connect to the database.")
            print(e)

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        self.conn, self.cursor = None, None

    def read_single_record(self, query):
        result = None
        self.open_connection()
        try:
            self.cursor.execute(query=query)
            result = self.cursor.fetchall()
            result = result[0]
        except psycopg2.Error as e:
            print("read single record failed.")
            print(e)
        finally:
            self.close_connection()
            return result

    def write_single_record(self, query):
        self.open_connection()
        try:
            self.cursor.execute(query=query)
            self.conn.commit()
        except psycopg2.Error as e:
            print("write single record failed.")
            print(e)
        finally:
            self.close_connection()
