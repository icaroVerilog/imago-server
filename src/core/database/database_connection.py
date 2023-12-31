import sqlite3 as SQL
import os

class DatabaseConnection:
    def __init__(self, database= os.getcwd() + "/core/database/database.db"):
        self._database = database
        self._connection = None
        
    
    def start_connection(self):
            self._connection = SQL.connect(self._database)
            cursor = self._connection.cursor()
            
            return cursor
    
    def commit_operation(self):
        # adicionar tratamento de excessões
        self._connection.commit()
    
    def finish_connection(self):
        try:
            self._connection.close()
        except SQL.Error:
            print("")