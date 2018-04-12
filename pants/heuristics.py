from math import sqrt
import random


class BreadthFirst:
    """
    RESULTS:
    ------------
    Max Size : 5
    Moves: 13
    Nodes Evaluated : 14927
    """

    def __init__(self, goal):
        pass

    def score(self, pants_path):
        return len(pants_path.states)


class Nada:
    def __init__(self, goal):
        pass

    def score(self, parg):
        return 1


class TrimmedBF:
    """
    This heuristic sets a very high score for any states previously seen.

    RESULTS:
    ------------
    Max Size: 5
    Size :              5
    Moves:              13
    Nodes Evaluated :   1941
    """

    def __init__(self, goal):
        self.goal = goal
        self.max = len(goal)**len(goal)

    def score(self, pants_path):
        state = pants_path.last_state.state
        for each in pants_path.states[:-1]:
            if state == each.state:
                return self.max
        return len(pants_path.states)


class Distance:
    """
    RESULTS:
    ------------
    Max Size: 19
    Size :              5   6   10   13     15      19
    Moves:              13  24  71   122    163     264
    Nodes Evaluated :   44  94  759  7259   11147   170231
    """

    def __init__(self, goal):
        self.goal = goal

    def score(self, pants_path):
        state = pants_path.last_state.state
        goal_distance = sum([abs(g - s) for g,s in zip(self.goal, state)])

        return goal_distance


class TrimmedDistance:
    """
    This heuristic sets a very high score for any states previously seen. 

    RESULTS:
    ------------
    Max Size: 5
    Size :              5
    Moves:              13
    Nodes Evaluated :   2345
    """
    def __init__(self, goal):
        self.goal = goal
        self.max = len(goal)**len(goal)

    def score(self, pants_path):
        state = pants_path.last_state.state
        for each in pants_path.states[:-1]:
            if state == each.state:
                return self.max
        return sum([abs(g - s) for g,s in zip(self.goal, state)])


class Inversions:
    """
    This heuristic counts the number of inversions in the state vector.

    RESULTS:
    ------------
    Max Size: 10
    Size :              5    6    10
    Moves:              17   25   83
    Nodes Evaluated :   135  144  96864
    """

    def __init__(self, goal):
        diff = goal[1] - goal[0]
        if goal[1] > goal[0]:
            self.direction = 'increase'
        elif goal[1] < goal[0]:
            self.direction = 'decrease'

    def score(self, pants_path):
        state = pants_path.last_state.state
        count = 0
        for index in range(len(state) - 1):
            if self.direction == 'increase' and state[index + 1] < state[index]:
                count += 1
            if self.direction == 'decrease' and state[index + 1] > state[index]:
                count += 1

        return count


class EuclideanDistance:
    """
    This heuristic calculates the Euclidean distance between the goal and state vectors.

    RESULTS:
    ------------
    Max Size: Between 100 and 200
    Size :              5   6   10   13     15      19      100
    Moves:              14  21  58   95     125     198     5107
    Nodes Evaluated :   31  55  170  290    383     617     15587
    """ 

    def __init__(self, goal):
        self.goal = goal

    def score(self, pants_path):
        state = pants_path.last_state.state
        distance = sqrt(sum([(g - s)**2 for g,s in zip(self.goal, state)]))

        return distance


class TrimmedED:
    """
    This heuristic is worse than just using Euclidean distance.

    RESULTS:
    ------------
    Max Size: ??
    Size :              5
    Moves:              13
    Nodes Evaluated :   1877
    """

    def __init__(self, goal):
        self.goal = goal
        self.max = len(goal)**len(goal)

    def score(self, pants_path):
        state = pants_path.last_state.state
        for each in pants_path.states[:-1]:
            if state == each.state:
                return self.max
        return sqrt(sum([(g - s)**2 for g,s in zip(self.goal, state)]))


class Mishmash:
    def __init__(self, goal):
        self.goal = goal
        size = len(goal) - 1
        half = int(size / 2)
        self.high = half+1
        self.low = half-1

    def score(self, pants_path):
        state = pants_path.last_state.state
        first_score = sum(state[:self.low])
        second_score = sum(state[self.high:])

        return second_score - first_score


class Pauls(Distance) :
    def score(self, pants_leg) :
        # array
        state = pants_leg.last_state.state
        # integer 0...len()
        pointer = pants_leg.last_state.pointer
        goal_scores = [abs(g - s) for g,s in zip(self.goal, state)]
        modifier = self.pointer_modifier(pointer, goal_scores)
        return sum(goal_scores) - (modifier * 1)

    def pointer_modifier(self, position, goal_scores) :
        return goal_scores[position]


class Bogo:
    def __init__(self, goal):
        self.goal = goal

    def score(self, pants_path):
        return random.randint(1, len(self.goal))
