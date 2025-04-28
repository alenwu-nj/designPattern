class ETLPipeline:

    def __init__(self):
        self.source = None
        self.transformation = None
        self.destination = None

    def __str__(self):
        return f"ETL Pipeline:\n  Source: {self.source}\n  Transformation: {self.transformation}\n  Destination: {self.destination}"


class ETLPipelineBuilder:

    def set_source(self, source):
        raise NotImplementedError

    def set_transformation(self, transformation):
        raise NotImplementedError

    def set_destination(self, destination):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError


class ConcreteETLPipelineBuilder(ETLPipelineBuilder):

    def __init__(self):
        self.pipeline = ETLPipeline()

    def set_source(self, source):
        self.pipeline.source = source
        return self

    def set_transformation(self, transformation):
        self.pipeline.transformation = transformation
        return self

    def set_destination(self, destination):
        self.pipeline.destination = destination
        return self

    def build(self):
        return self.pipeline


class ETLPipelineDirector:

    def __init__(self, builder):
        self.builder = builder

    def construct_pipeline(self, source, transformation, destination):
        return (self.builder
                .set_source(source)
                .set_transformation(transformation)
                .set_destination(destination)
                .build())


if __name__ == '__main__':
    builder = ConcreteETLPipelineBuilder()
    director = ETLPipelineDirector(builder)
    pipeline = director.construct_pipeline("source", "transformation", "destination")
    print(pipeline)
