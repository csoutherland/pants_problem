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

    def __lt__(self, other):
        # TODO:  Explain this!
        return len(self.states) < len(other.states)
