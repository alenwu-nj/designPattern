from enum import Enum


class EventType(Enum):

    A = "A"
    B = "B"

class Mediator:
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):

    def __init__(self, component1, component2):
        self.component1 = component1
        self.component1.mediator = self
        self.component2 = component2
        self.component2.mediator = self

    def notify(self, sender, event):
        if event == EventType.A:
            print("Mediator reacts on A and triggers following operations:")
            self.component2.do_something()
        elif event == EventType.B:
            print("Mediator reacts on B and triggers following operations:")
            self.component1.do_something()


class Component1:

    def __init__(self):
        self.mediator = None

    def do_something(self):
        print("Component1 does something.")

    def trigger_event_a(self):
        print("Component1 triggers event A.")
        self.mediator.notify(self, EventType.A)


class Component2:

    def __init__(self):
        self.mediator = None

    def do_something(self):
        print("Component2 does something.")

    def trigger_event_b(self):
        print("Component2 triggers event B.")
        self.mediator.notify(self, EventType.B)


if __name__ == "__main__":

    component1 = Component1()
    component2 = Component2()
    mediator = ConcreteMediator(component1, component2)

    component1.trigger_event_a()
    component2.trigger_event_b()
