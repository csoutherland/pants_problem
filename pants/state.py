class PantsState:

    def __init__(self, pointer, state):
        self.pointer = pointer
        self.state = state

    def move_pointer_left(self):
        if self.pointer > 1:
            return PantsState(self.pointer - 2, self.state)
        else:
            return None

    def move_pointer_right(self):
        if self.pointer < len(self.state) - 2:
            return PantsState(self.pointer + 2, self.state)
        else:
            return None

    def swap_left(self):
        if self.pointer > 0:
            new_state = self.state[:]
            new_state[self.pointer - 1], new_state[self.pointer] = new_state[self.pointer], new_state[self.pointer - 1]
            return PantsState(self.pointer - 1, new_state)
        else:
            return None

    def swap_right(self):
        if self.pointer < len(self.state) - 1:
            new_state = self.state[:]
            new_state[self.pointer + 1], new_state[self.pointer] = new_state[self.pointer], new_state[self.pointer + 1]
            return PantsState(self.pointer + 1, new_state)
        else:
            return None

    def __str__(self):
        elements = [str(v) if i != self.pointer else '*{}'.format(v) for i,v in enumerate(self.state)]
        return '[{}]'.format(' '.join(elements))

    def __eq__(self, other):
        if isinstance(other, PantsState):
            return self.pointer == other.pointer and self.state == other.state
        else:
            return False
