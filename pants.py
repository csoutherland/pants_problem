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

    @property
    def last_state(self):
        return self.states[-1]

    @property
    def children(self):
        state_transitions = [
            self.last_state.move_pointer_left,
            self.last_state.move_pointer_right,
            self.last_state.swap_left,
            self.last_state.swap_right
        ]

        for transition in state_transitions:
            next_state = transition()

            # Only if the next state is a valid move AND we have not been in
            # this position before, make a new path with the transition
            if next_state is not None and next_state not in self.states:
                yield PantsPath(self.states + [next_state])

    def __str__(self):
        return '\n'.join([str(state) for state in self.states])

    def __eq__(self, other):
        if isinstance(other, PantsPath):
            return self.states == other.states
        else:
            return False

class PantsSolver:

    def __init__(self, initial, goal):
        self.working_set = [PantsPath([PantsState(0, initial)])]
        self.goal = goal

    def solve(self):
        evaluated = 0
        while len(self.working_set) > 0:
            best = self.working_set.pop(0)
            evaluated += 1

            # TODO:  Should this be a method?
            if best.last_state.state == self.goal:
                print('Solved!')
                print('Nodes evaluated:  {}'.format(evaluated))
                print('Moves:  {}'.format(len(best.states) - 1))
                print(str(best))

                return
            else:
                self.working_set += list(best.children)


def run():
    solver = PantsSolver(
        initial=[1, 2, 3, 4, 5],
        goal=[5, 4, 3, 2, 1]
    )

    solver.solve()

if __name__ == '__main__':
    run()
