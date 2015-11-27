import argparse

from pants.solver import PantsSolver
from pants import heuristics


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
    parser = argparse.ArgumentParser(description='Solve the Pants Problem.')
    parser.add_argument('--size', type=int, default=5, help='The size of the problem set (defaults to 5)')
    parser.add_argument('--heuristic', default='BreadthFirst', help='The heuristc class to use.')

    args = parser.parse_args()

    initial = list(range(1, args.size + 1))
    goal = list(reversed(initial))

    print('Initial state:  {}'.format(initial))
    print('Goal state  {}:'.format(goal))

    heuristic = getattr(heuristics, args.heuristic, None)

    if heuristic and type(heuristic) is type:
        print('Heuristic:  {}'.format(args.heuristic))

        solver = PantsSolver(
            initial=initial,
            goal=goal,
            heuristic=heuristic(goal)
        )

        solver.solve()
        display(solver)
    else:
        print('ERROR:  Cannot find heuristic with name "{}"'.format(args.heuristic))


if __name__ == '__main__':
    run()
