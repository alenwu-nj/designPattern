class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        print("Creating a new instance of Singleton")

    def someMethod(self):
        print("This is a singleton method")


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    s1.someMethod()
    s2.someMethod()
