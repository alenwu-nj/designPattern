class Memento:

    def __init__(self, state):
        self.state = state


class Originator:

    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state
        print(f"set state: {self.state}")

    def save_state(self):
        return Memento(self.state)

    def restore_state(self, memento):
        self.state = memento.state
        print(f"restore state: {self.state}")


class Caretaker:

    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("state1")
    caretaker.add_memento(originator.save_state())

    originator.set_state("state2")
    caretaker.add_memento(originator.save_state())

    originator.set_state("state3")

    originator.restore_state(caretaker.get_memento(0))
