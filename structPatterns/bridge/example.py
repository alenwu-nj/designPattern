class DataSource:

    def extract(self):
        pass


class DatabaseSource(DataSource):

    def extract(self):
        print("loading data from database")


class APISource(DataSource):

    def extract(self):
        print("loading data from API")


class ETLProcess:

    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def extract(self):
        self.data_source.extract()

    def transform(self):
        print("data transformation")

    def load(self):
        print("data loading")


class DataSourceETL(ETLProcess):
    def run(self):
        self.extract()
        self.transform()
        self.load()


db_etl = DataSourceETL(DatabaseSource())
db_etl.run()

api_etl = DataSourceETL(APISource())
api_etl.run()
