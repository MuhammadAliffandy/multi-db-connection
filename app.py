import sqlite3
import psycopg2
import pymysql

# class factory pattern

class DatabaseConnection:
    def connect(self):
        pass

class SQLiteDatabaseConnection(DatabaseConnection):
    def connect(self, database_name):
        return sqlite3.connect(database_name)

class PostgreSQLDatabaseConnection(DatabaseConnection):
    def connect(self, host, database, user, password , port):
        return psycopg2.connect(host=host, database=database, user=user, password=password ,port=port)

class MySQLDatabaseConnection(DatabaseConnection):
    def connect(self, host, database, user, password , port ):
        return pymysql.connect(host=host, database=database, user=user, password=password , port = port)

# class databases logical operation

class DatabaseConnectionFactory:

    def __init__ (self,db_type = None):
        self.db_type = db_type

    def create_connection(self):
        if self.db_type == 1:
            return SQLiteDatabaseConnection().connect()
        elif self.db_type == 2 :
            return PostgreSQLDatabaseConnection().connect()
        elif self.db_type == 3 :
            return MySQLDatabaseConnection().connect()
        else:
            raise ValueError("Invalid database type")

# machine cli ui

print('===== SILAHKAN PILIH DATABASE CONNECTION ANDA =====\n')

db_list = ['1. SQLITE' , '2. POSTGRESQL' , '3. MYSQL']

for data in db_list:
    print(data)

answer = int(input('\nMasukkan type databasenya (pilih angka) : '))

if( answer < 4 and answer > 0):
    print(f'Database Status : {DatabaseConnectionFactory(answer)}')
else:
    print('Keyword yang anda masukkan salah')




