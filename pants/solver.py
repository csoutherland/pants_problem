from heapq import heappush, heappop

from pants.state import PantsState
from pants.path import PantsPath

class PantsSolver:

    def __init__(self, initial, goal, heuristic):
        self.working_set = []
        self.goal = goal
        self.heuristic = heuristic

        self.add_path(PantsPath([PantsState(0, initial)]))

    def add_path(self, path):
        heappush(self.working_set, (self.heuristic.score(path), path))

    def solve(self):
        evaluated = 0
        while len(self.working_set) > 0:
            score, best = heappop(self.working_set)
            evaluated += 1

            # TODO:  Should this be a method?
            if best.last_state.state == self.goal:
                return (best, evaluated)
            else:
                for child in best.children:
                    self.add_path(child)
