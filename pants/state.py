class PantsState:
    """
    An individual state of the Pants Problem.

    There are two main attributes of a PantsState:
    1) The 'state' represented as a list of numbers
    2) A pointer, which is an integer representing the current position in the state

    There are four actions that can be made:
    1) Move the pointer two positions to the left
    2) Move the pointer two positions to the right
    3) Swap the position under the pointer to the left
    4) Swap the position under the pointer to the right

    These actions are documented in greater detail in their respective methods.
    """

    def __init__(self, pointer, state):
        """
        Initialization method for PantsState

        Args:
            pointer (int):      The current position of the pointer (0 indexed)
            state (list[int]):  The state list - this is the state to be manipulated by further actions
        """
        self.pointer = pointer
        self.state = state

    def move_pointer_left(self):
        """
        Move the pointer two positions to the left, if possible.

        Returns:
            A new PantsState with the pointer moved two positions to the left,
            or None if the pointer cannot be moved.
        """
        if self.pointer > 1:
            return PantsState(self.pointer - 2, self.state)
        else:
            return None

    def move_pointer_right(self):
        """
        Move the pointer two positions to the right, if possible.

        Returns:
            A new PantsState with the pointer moved two positions to the right,
            or None if the pointer cannot be moved.
        """
        if self.pointer < len(self.state) - 2:
            return PantsState(self.pointer + 2, self.state)
        else:
            return None

    def swap_left(self):
        """
        Swap the position under the pointer with the position to the left.

        Example:
            If the current state is:              [3 2 5 *1 4]
            Calling 'swap_left' would result in:  [3 2 *1 5 4]

        Returns:
            A new PantsState representing the positions swapped, or None if the position cannot be swapped to the left.
        """
        if self.pointer > 0:
            new_state = self.state[:]
            new_state[self.pointer - 1], new_state[self.pointer] = new_state[self.pointer], new_state[self.pointer - 1]
            return PantsState(self.pointer - 1, new_state)
        else:
            return None

    def swap_right(self):
        """
        Swap the position under the pointer with the position to the right.

        Example:
            If the current state is:               [3 2 5 *1 4]
            Calling 'swap_right' would result in:  [3 2 5 4 *1]

        Returns:
            A new PantsState representing the positions swapped, or None if the position cannot be swapped to the right.
        """
        if self.pointer < len(self.state) - 1:
            new_state = self.state[:]
            new_state[self.pointer + 1], new_state[self.pointer] = new_state[self.pointer], new_state[self.pointer + 1]
            return PantsState(self.pointer + 1, new_state)
        else:
            return None

    def __str__(self):
        """
        Return a string representation of this PantsState.

        Example:
            >> str(PantsState(2, [5, 4, 3, 2, 1]))
            >> '[5 4 *3 2 1]'
        """
        elements = [str(v) if i != self.pointer else '*{}'.format(v) for i,v in enumerate(self.state)]
        return '[{}]'.format(' '.join(elements))

    def __eq__(self, other):
        """
        Determine if two PantsStates are equal.

        Example:
            >> PantsState(3, [2, 3, 4, 5, 1]) == PantsState(3, [2, 3, 4, 5, 1])
            >> True

            >> # Different pointer positions means they are not equal
            >> PantsState(2, [2, 3, 4, 5, 1]) == PantsState(3, [2, 3, 4, 5, 1])
            >> False

            >> # Of course, different state lists are also not equal
            >> PantsState(3, [1, 3, 4, 5, 2]) == PantsState(3, [2, 3, 4, 5, 1])
            >> False
        """
        if isinstance(other, PantsState):
            return self.pointer == other.pointer and self.state == other.state
        else:
            return False
