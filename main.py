"""
This script generates solutions to the equation -t^2 + x^2 + y^2 = 1 using the Z3 SMT solver from Microsoft Research.

Bounds for all three variables as well as a maximum number of desired solutions can be set.
"""

from z3 import *

# x min/max bounds
X_MIN = -20000
X_MAX = 20000

# y min/max bounds
Y_MIN = -20000
Y_MAX = 20000

# t min/max bounds
T_MIN = -20000
T_MAX = 20000

# maximum number of solutions to find
MAX_SOLUTIONS = 250

if __name__ == '__main__':
    # create Z3 variables
    x, y, t = Ints('x y t')

    # create Z3 solver
    s = Solver()

    # add constraints
    s.add(-(t ** 2) + (x ** 2) + (y ** 2) == 1)
    s.add(x >= X_MIN)
    s.add(x <= X_MAX)
    s.add(y >= Y_MIN)
    s.add(y <= Y_MAX)
    s.add(t >= T_MIN)
    s.add(t <= T_MAX)

    # find solutions
    solutions = []
    while s.check() == sat and len(solutions) < MAX_SOLUTIONS:
        # get model
        m = s.model()

        # get solution
        solution = (m[x].as_long(), m[y].as_long(), m[t].as_long())

        # check if solution fulfills constraints
        assert -(solution[2] ** 2) + (solution[0] ** 2) + (solution[1] ** 2) == 1

        # add solution to list
        solutions.append(solution)

        # print solution
        print(f"x: {solution[0]}  y: {solution[1]}  t: {solution[2]}")

        # add constraint to exclude current solution in the next iteration
        s.add(Or(x != solution[0], y != solution[1], t != solution[2]))

    # write solutions to a csv file
    with open('solutions.csv', 'w') as f:
        f.write("x,y,t\n")
        for solution in solutions:
            f.write(f"{solution[0]},{solution[1]},{solution[2]}\n")
