from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class ConcretePrototypeA(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototypeB(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    prototype_a = ConcretePrototypeA("Prototype A")
    prototype_b = ConcretePrototypeB("Prototype B")

    clone_a = prototype_a.clone()
    clone_b = prototype_b.clone()

    clone_a.value = "Modified Clone A"
    clone_b.value = "Modified Clone B"

    print(f"Original: {prototype_a.value}, Clone: {clone_a.value}")
    print(f"Original: {prototype_b.value}, Clone: {clone_b.value}")
