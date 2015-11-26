class PantsPath:
    """
    A series of PantsStates representing a progression of moves.
    """

    def __init__(self, states):
        """
        Initialization method for PantsPath

        Args:
            states (list[PantsState]):  The ordered list of PantsStates, presenting the movement history
        """
        self.states = states

    @property
    def last_state(self):
        return self.states[-1]

    @property
    def children(self):
        """
        Generate the next set of PantsPaths with valid moves from the last PantsState in the series.

        Returns:
            A list of new PantsPaths, each with one additional PantsState for each valid move from the most recent PantsState.
        """
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
        """
        Return a string representation of this PantsPath.

        Returns:
            A multiline string with each PantsState on a separate line.
        """
        return '\n'.join([str(state) for state in self.states])

    def __eq__(self, other):
        """
        Determine if two PantsPaths are equal.
        """
        if isinstance(other, PantsPath):
            return self.states == other.states
        else:
            return False

    def __lt__(self, other):
        """
        Define an ordering for two different PantsPaths.

        This serves as the basis for any sorting of PantsPaths.
        While the heuristics guide the exploring of the problem
        set, the implementation of python's priority queue needs
        this to be defined.
        """
        return len(self.states) < len(other.states)
