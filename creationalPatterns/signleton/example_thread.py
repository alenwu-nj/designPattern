# This is an example of a thread-safe singleton class in Python.
import threading


class SingletonMeta(type):

    _instances = {}

    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        print("Creating an instance of Singleton")

    def someMethod(self):
        print("This is an example method of Singleton")

# Usage:
s1 = Singleton()
s2 = Singleton()
s1.someMethod()
s2.someMethod()