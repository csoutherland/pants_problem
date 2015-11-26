from pants.solver import PantsSolver
from pants.heuristics import BreadthFirstHeuristic, DistanceHeuristic


def display(path, evaluated):
    print('Solved!')
    print('Nodes evaluated:  {}'.format(evaluated))
    print('Moves:  {}'.format(len(path.states) - 1))
    print(str(path))


def run():
    initial = [1, 2, 3, 4, 5]
    goal = [5, 4, 3, 2, 1]

    solver = PantsSolver(initial, goal,
        heuristic=BreadthFirstHeuristic()
    )

    print('------ Breadth First -----------------')
    display(*solver.solve())

    solver = PantsSolver(initial, goal,
        heuristic=DistanceHeuristic(goal)
    )

    print('------ Distance Search -----------------')
    display(*solver.solve())

    initial = [1, 2, 3, 4, 5, 6, 7]
    goal = [7, 6, 5, 4, 3, 2, 1]

    solver = PantsSolver(initial, goal,
        heuristic=DistanceHeuristic(goal)
    )

    print('------ Big Distance Search -----------------')
    display(*solver.solve())

if __name__ == '__main__':
    run()
