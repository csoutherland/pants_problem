import unittest
from pants.state import PantsState
from pants.path import PantsPath

class PantsPathTest(unittest.TestCase):

    def test_all_children_generated(self):
        initial_state = PantsState(2, [1, 2, 3, 4, 5])
        initial_path = PantsPath([initial_state])

        actual_child_paths = list(initial_path.children)

        expected_paths = [
            PantsPath([initial_state, PantsState(0, [1, 2, 3, 4, 5])]),
            PantsPath([initial_state, PantsState(4, [1, 2, 3, 4, 5])]),
            PantsPath([initial_state, PantsState(1, [1, 3, 2, 4, 5])]),
            PantsPath([initial_state, PantsState(3, [1, 2, 4, 3, 5])])
        ]

        self.assertEqual(expected_paths, actual_child_paths)

    def test_only_right_children_generated(self):
        initial_state = PantsState(0, [1, 2, 3, 4, 5])
        initial_path = PantsPath([initial_state])

        actual_child_paths = list(initial_path.children)

        expected_paths = [
            PantsPath([initial_state, PantsState(2, [1, 2, 3, 4, 5])]),
            PantsPath([initial_state, PantsState(1, [2, 1, 3, 4, 5])])
        ]

        self.assertEqual(expected_paths, actual_child_paths)

    def test_only_left_children_generated(self):
        initial_state = PantsState(4, [1, 2, 3, 4, 5])
        initial_path = PantsPath([initial_state])

        actual_child_paths = list(initial_path.children)

        expected_paths = [
            PantsPath([initial_state, PantsState(2, [1, 2, 3, 4, 5])]),
            PantsPath([initial_state, PantsState(3, [1, 2, 3, 5, 4])])
        ]

        self.assertEqual(expected_paths, actual_child_paths)

    def test_skip_children_if_already_in_path(self):
        initial_states = [
            PantsState(0, [1, 2, 3, 4, 5]),
            PantsState(1, [2, 1, 3, 4, 5]),
        ]
        initial_path = PantsPath(initial_states)

        actual_child_paths = list(initial_path.children)

        expected_paths = [
            PantsPath(initial_states + [PantsState(3, [2, 1, 3, 4, 5])]),
            PantsPath(initial_states + [PantsState(2, [2, 3, 1, 4, 5])])
        ]

        self.assertEqual(expected_paths, actual_child_paths)
