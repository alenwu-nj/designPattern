class Checkpoint:

    def __init__(self, state):
        self.state = state

    def restore(self):
        print(f"restored: {self.state}")


class CheckpointFactory:

    def __init__(self):
        self.checkpoints = {}

    def get_checkpoint(self, state):
        if state not in self.checkpoints:
            self.checkpoints[state] = Checkpoint(state)
        return self.checkpoints[state]


class CheckpointManager:

    def __init__(self):
        self.factory = CheckpointFactory()
        self.checkpoint_history = []

    def create_checkpoint(self, state):
        checkpoint = self.factory.get_checkpoint(state)
        self.checkpoint_history.append(checkpoint)
        print(f"created checkpoint: {state}")

    def restore_checkpoint(self, index):
        if 0 <= index < len(self.checkpoint_history):
            self.checkpoint_history[index].restore()
        else:
            print("invalid checkpoint index")

    def delete_checkpoint(self, index):
        if 0 <= index < len(self.checkpoint_history):
            print(f"deleted checkpoint: {self.checkpoint_history[index].state}")
            del self.checkpoint_history[index]
        else:
            print("invalid checkpoint index")

    def list_checkpoints(self):
        print("current checkpoints:")
        for i, checkpoint in enumerate(self.checkpoint_history):
            print(f"{i}: {checkpoint.state}")


def client_code():
    manager = CheckpointManager()

    manager.create_checkpoint("state_A")
    manager.create_checkpoint("state_B")
    manager.create_checkpoint("state_C")

    manager.list_checkpoints()

    manager.restore_checkpoint(1)

    manager.delete_checkpoint(0)

    manager.list_checkpoints()


if __name__ == "__main__":

    client_code()
