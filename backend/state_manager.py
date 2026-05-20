class StateManager:
    def __init__(self):
        self.state = {
            "workflow_status": "initialized"
        }

    def update(self, key, value):
        self.state[key] = value

    def get_state(self):
        return self.state
