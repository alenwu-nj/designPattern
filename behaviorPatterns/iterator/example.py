class DataSource:

    def extract(self, data):
        pass


class DatabaseSource(DataSource):

    def extract(self, data):
        print("loading data from database")
        for item in data:
            yield item


class APISource(DataSource):

    def extract(self, data):
        print("loading data from API")
        for item in data:
            yield item


class ETLProcess:

    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def extract(self, data):
        yield from self.data_source.extract(data)

    def transform(self, data):
        print("data transformation")
        data += " (transformed)"
        yield data

    def load(self, data):
        print("data loading")
        data += " (loaded)"
        yield data


class DataSourceETL(ETLProcess):

    def run(self, data: list):
        print("running ETL process")
        for item in self.extract(data):
            for transformed_item in self.transform(item):
                for loaded_item in self.load(transformed_item):
                    print(loaded_item)


if __name__ == "__main__":
    data = ["data1", "data2", "data3"]
    db_etl = DataSourceETL(DatabaseSource())
    db_etl.run(data)

    api_etl = DataSourceETL(APISource())
    api_etl.run(data)
