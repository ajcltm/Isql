from typing import Protocol
import pymysql
import sqlite3



class IConnection(Protocol):

    def execute(self):
        pass

class MySqlConnector:

    def __init__(self, dbName:str) -> None:
        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='2642805', db=dbName, charset='utf8')
    
    def execute(self):
        return self.db

class SqliteConnector:

    def __init__(self, fileDir:str) -> None:
        self.db = sqlite3.connect(fileDir)
    
    def execute(self):
        return self.db


def get_connector(kind, var):

    option = {
        'mysql':MySqlConnector,
        'Sqlite':SqliteConnector
        }
    
    IConnection = option.get(kind)

    return IConnection(var).execute()


