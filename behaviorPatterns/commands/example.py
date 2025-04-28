from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class DataReceiver:
    def process_data(self, action):
        print(f"doing something with: {action}")


class SimpleCommand(Command):
    def __init__(self, receiver, action):
        self.receiver = receiver
        self.action = action

    def execute(self):
        self.receiver.process_data(self.action)


class ComplexCommand(Command):
    def __init__(self, receiver, *actions):
        self.receiver = receiver
        self.actions = actions

    def execute(self):
        for action in self.actions:
            self.receiver.process_data(action)


class Invoker:
    def __init__(self):
        self.start_command = None
        self.finish_command = None

    def set_on_start(self, command):
        self.start_command = command

    def set_on_finish(self, command):
        self.finish_command = command

    def do_something_important(self):
        if self.start_command:
            self.start_command.execute()
        if self.finish_command:
            self.finish_command.execute()


if __name__ == "__main__":
    receiver = DataReceiver()
    invoker = Invoker()

    invoker.set_on_start(SimpleCommand(receiver, "Say Hi!"))

    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))

    invoker.do_something_important()
