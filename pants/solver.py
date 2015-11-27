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
            max_iterations (int): The maximum number of iterations to evaluate when solving the problem
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
        """
        Pops the best (lowest score) PantsPath from the priority queue.

        Returns:
            The PantsPath from the working set with the lowest score.
        """
        # Ignoring the score for now...
        score, path = heappop(self.working_set)

        return path

    @property
    def solved(self):
        """
        Is there a solution for the current problem?

        Returns:
            True if a solution has been found, False otherwise
        """
        return self.solution is not None

    def iterate(self):
        """
        Performs a single cycle of the solution algorithm.

        The algorithm is as follows:
        1) Find the "best" PantsPath from the working set
        2) Evaluate if the PantsPath results in the goal state
        3) If not, generate child nodes representing all additional
           valid moves, and add them to the working set
        """
        best = self.pop_best()

        # TODO:  Should this be a method on PantsState?
        if best.last_state.state == self.goal:
            self.solution = best
        else:
            for path in best.children:
                self.add_path(path)

    def solve(self):
        """
        Attempt to solve the pants problem.

        This simply calls `iterate()` until one of two
        conditions occur:
        1) A solution is found
        2) The number of calls to `iterate()` exceeds `max_iterations`
        """
        for _ in range(self.max_iterations):
            if self.solved:
                return
            else:
                self.iterate()
