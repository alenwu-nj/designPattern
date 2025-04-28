from abc import ABC, abstractmethod
from typing import List


class DataComponent(ABC):

    @abstractmethod
    def process(self, data):
        pass


class DataCleaning(DataComponent):

    def process(self, data):
        return data


class DataTransformation(DataComponent):

    def process(self, data):
        return data


class DataLoading(DataComponent):

    def process(self, data):
        return data


class ETLPipeline(DataComponent):

    def __init__(self):
        self.components: List[DataComponent] = []

    def add(self, component: DataComponent):
        self.components.append(component)

    def process(self, data):
        for component in self.components:
            data = component.process(data)
        return data


if __name__ == "__main__":

    pipeline = ETLPipeline()
    pipeline.add(DataCleaning())
    pipeline.add(DataTransformation())
    pipeline.add(DataLoading())

    raw_data = "some raw data"
    pipeline.process(raw_data)
