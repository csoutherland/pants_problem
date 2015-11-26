from heapq import heappush, heappop

from pants.state import PantsState
from pants.path import PantsPath

class PantsSolver:
    """
    Represents a Pants Problem, and a heuristic for exploring the problem space.

    There are three main attributes:
    1) Initial state, as a list
    2) Goal state, as a list
    3) A heuristic for exploring the problem set
    """

    def __init__(self, initial, goal, heuristic, max_iterations=100000):
        """
        Initialization method for PantsSolver

        Args:
            initial (list[int]):  The initial state of the problem
            goal (list[int]):     The desired goal state of the problem
            heuristic (object):   An object that implements a 'score' method for evaluating PantsPaths
        """
        self.working_set = []
        self.goal = goal
        self.heuristic = heuristic
        self.evaluated = 0
        self.solution = None
        self.max_iterations = max_iterations

        # Seed the working set with a single PantsPath, starting at position 0
        self.add_path(PantsPath([PantsState(0, initial)]))

    def add_path(self, path):
        """
        Add a new PantsPath to the working set.

        Note:  This uses the heuristic to score the PantsPath when adding to the
               underlying priority queue
        """
        heappush(self.working_set, (self.heuristic.score(path), path))
        self.evaluated += 1

    def pop_best(self):
        # Ignoring the score for now...
        score, path = heappop(self.working_set)

        return path

    @property
    def solved(self):
        return self.solution is not None

    def iterate(self):
        best = self.pop_best()

        # TODO:  Should this be a method on PantsState?
        if best.last_state.state == self.goal:
            self.solution = best
        else:
            for child in best.children:
                self.add_path(child)

    def solve(self):
        for _ in range(self.max_iterations):
            if self.solved:
                return
            else:
                self.iterate()
