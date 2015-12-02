import unittest

from pants.state import PantsState
from pants.path import PantsPath
from pants.solver import PantsSolver
from pants.heuristics import BreadthFirst


class PantsSolverTest(unittest.TestCase):

    def setUp(self):
        self.solver = PantsSolver(
            initial=[1, 2, 3, 4, 5],
            goal=[5, 4, 3, 2, 1],
            heuristic=BreadthFirst(None)
        )


    def test_initial_setup(self):
        self.assertEqual(1, self.solver.evaluated)
        self.assertEqual(1, len(self.solver.working_set))

    def test_pop_best(self):
        best = self.solver.pop_best()

        self.assertEqual(PantsPath([PantsState(0, [1, 2, 3, 4, 5])]), best)
        self.assertEqual([], self.solver.working_set)

    def test_next_iteration(self):
        self.solver.iterate()

        self.assertEqual(3, self.solver.evaluated)

        best = self.solver.pop_best()
        expected_best = PantsPath([
            PantsState(0, [1, 2, 3, 4, 5]),
            PantsState(2, [1, 2, 3, 4, 5])
        ])

        self.assertEqual(expected_best, best)
