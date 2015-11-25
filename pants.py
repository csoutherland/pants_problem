
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

    @property
    def is_solved(self):
        return self.state == list(reversed(sorted(self.state)))

    def __str__(self):
        elements = [str(v) if i != self.pointer else '*{}'.format(v) for i,v in enumerate(self.state)]
        return '[{}]'.format(' '.join(elements))

    def __eq__(self, other):
        if isinstance(other, PantsState):
            return self.pointer == other.pointer and self.state == other.state
        else:
            return False


class PantsPath:

    def __init__(self, states):
        self.states = states

    def next_states(self):
        last_state = self.states[-1]

        next_states = [
            last_state.move_pointer_right(),
            last_state.move_pointer_left(),
            last_state.swap_right(),
            last_state.swap_left()
        ]

        # TODO:  Optimize this - this is a linear check in the history
        return [s for s in next_states if s is not None and s not in self.states]

    def generate_children(self):
        children = []
        for state in self.next_states():
            new_states = self.states[:]
            new_states.append(state)

            children.append(PantsPath(new_states))

        return children

    @property
    def is_solved(self):
        return self.states[-1].is_solved

    def __str__(self):
        return ' -> '.join([str(state) for state in self.states])

    def __eq__(self, other):
        return self.states == other.states


def run():
    initial_state = PantsState(0, [1, 2, 3, 4, 5])

    layer = [PantsPath([initial_state])]

    while len(layer) > 0:
        # Loop over the tree one layer at a time - this could be improved!
        for path in layer:
            if path.is_solved:
                print('Solved!')
                print('Moves:  {}'.format(len(path.states) - 1))
                print(str(path))

                return

        next_layer = []
        for path in layer:
            next_layer.extend(path.generate_children())

        layer = next_layer

    print('No solution found...')


if __name__ == '__main__':
    run()
