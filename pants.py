from pants.solver import PantsSolver
from pants.heuristics import BreadthFirstHeuristic, DistanceHeuristic


def display(solver):
    if solver.solved:
        print('Solved!')
        print('Nodes evaluated:  {}'.format(solver.evaluated))
        print('Moves:  {}'.format(len(solver.solution.states) - 1))
        print(str(solver.solution))
    else:
        print('No solution found...')
        print('Nodes evaluated:  {}'.format(solver.evaluated))


def run():
    initial = [1, 2, 3, 4, 5]
    goal = [5, 4, 3, 2, 1]

    solver = PantsSolver(initial, goal,
        heuristic=BreadthFirstHeuristic()
    )

    print('------ Breadth First -----------------')
    solver.solve()
    display(solver)

    solver = PantsSolver(initial, goal,
        heuristic=DistanceHeuristic(goal)
    )

    print('------ Distance Search -----------------')
    solver.solve()
    display(solver)

    initial = [1, 2, 3, 4, 5, 6, 7]
    goal = [7, 6, 5, 4, 3, 2, 1]

    solver = PantsSolver(initial, goal,
        heuristic=BreadthFirstHeuristic()
    )

    print('------ Big Breadth First -----------------')
    solver.solve()
    display(solver)

    solver = PantsSolver(initial, goal,
        heuristic=DistanceHeuristic(goal)
    )

    print('------ Big Distance Search -----------------')
    solver.solve()
    display(solver)

if __name__ == '__main__':
    run()
