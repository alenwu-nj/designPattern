from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def process_data(self):
        self.load_data()
        self.clean_data()
        self.transform_data()
        self.save_data()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def clean_data(self):
        pass

    @abstractmethod
    def transform_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass


class CSVDataProcessor(DataProcessor):

    def load_data(self):
        print("loading CSV data")

    def clean_data(self):
        print("cleaning CSV data")

    def transform_data(self):
        print("transforming CSV data")

    def save_data(self):
        print("saving CSV data")


class JSONDataProcessor(DataProcessor):

    def load_data(self):
        print("loading JSON data")

    def clean_data(self):
        print("cleaning JSON data")

    def transform_data(self):
        print("transforming JSON data")

    def save_data(self):
        print("saving JSON data")


if __name__ == "__main__":
    csv_processor = CSVDataProcessor()
    csv_processor.process_data()

    print("\n")

    json_processor = JSONDataProcessor()
    json_processor.process_data()
