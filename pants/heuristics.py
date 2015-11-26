
class BreadthFirstHeuristic:

    def score(self, pants_path):
        return len(pants_path.states)


class DistanceHeuristic:

    def __init__(self, goal):
        self.goal = goal

    def score(self, pants_path):
        state = pants_path.last_state.state
        goal_distance = sum([abs(g - s) for g,s in zip(self.goal, state)])

        return goal_distance
