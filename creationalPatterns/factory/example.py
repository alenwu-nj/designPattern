from abc import ABC, abstractmethod
from enum import Enum


class DatabaseType(Enum):

    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    ORACLE = "oracle"


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def findAll(self):
        pass

class MySQL(Database):

    def connect(self):
        print("Connected to MySQL")

    def insert(self, data):
        print("Inserted data into MySQL")

    def findAll(self):
        print("Finding all data from MySQL")



class PostgreSQL(Database):

    def connect(self):
        print("Connected to PostgreSQL")

    def insert(self, data):
        print("Inserted data into PostgreSQL")

    def findAll(self):
        print("Finding all data from PostgreSQL")

class Oracle(Database):

    def connect(self):
        print("Connected to Oracle")

    def insert(self, data):
        print("Inserted data into Oracle")

    def findAll(self):
        print("Finding all data from Oracle")


class Factory:

    def create_database(self, database_type):
        if database_type == DatabaseType.MYSQL:
            return MySQL()
        elif database_type == DatabaseType.POSTGRESQL:
            return PostgreSQL()
        elif database_type == DatabaseType.ORACLE:
            return Oracle()
        else:
            raise ValueError("Invalid database type")


if __name__ == "__main__":
    factory = Factory()
    database = factory.create_database(DatabaseType.MYSQL)
    database.connect()
    database.insert("data")
