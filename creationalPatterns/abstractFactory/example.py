from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(ABC):

    @abstractmethod
    def feature(self):
        pass


class ConcreteProductA1(AbstractProductA):

    def feature(self):
        return "Product A1"


class ConcreteProductA2(AbstractProductA):

    def feature(self):
        return "Product A2"


class AbstractProductB(ABC):

    @abstractmethod
    def feature(self):
        pass


class ConcreteProductB1(AbstractProductB):

    def feature(self):
        return "Product B1"


class ConcreteProductB2(AbstractProductB):

    def feature(self):
        return "Product B2"


class Client:

    def __init__(self, factory):
        if not isinstance(factory, AbstractFactory):
            raise TypeError("Expected object of type AbstractFactory or its subclass.")
        self.factory = factory

    def run(self):
        try:
            product_a = self.factory.create_product_a()
            product_b = self.factory.create_product_b()
            print(product_a.feature())
            print(product_b.feature())
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        factory1 = ConcreteFactory1()
        client1 = Client(factory1)
        client1.run()

        factory2 = ConcreteFactory2()
        client2 = Client(factory2)
        client2.run()
    except Exception as e:
        print(f"An error occurred in main: {e}")
