class DataHandler:

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, data):
        if self.successor:
            self.successor.handle(data)


class DataCleaner(DataHandler):

    def handle(self, data):
        print("cleaning data...")

        super().handle(data)


class DataTransformer(DataHandler):

    def handle(self, data):
        print("transforming data...")

        super().handle(data)


class DataLoader(DataHandler):

    def handle(self, data):
        print("loading data...")

        super().handle(data)


def client_code():

    loader = DataLoader()
    transformer = DataTransformer(loader)
    cleaner = DataCleaner(transformer)

    data = "raw data"
    cleaner.handle(data)


if __name__ == "__main__":
    client_code()
