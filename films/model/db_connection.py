import sqlite3


class Connection:
    def __init__(self):
        self.database = "database/movies.db"
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.commit()
        self.connection.close()
