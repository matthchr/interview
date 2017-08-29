import solver


def test_load_maze():
    # TODO: Fill this in
    assert False


def test_solve_maze1():
    maze = solver.load_maze('maze1.txt')
    result = solver.solve(maze)
    assert result is True


def test_solve_maze2():
    maze = solver.load_maze('maze2.txt')
    result = solver.solve(maze)
    assert result is True


def test_solve_maze3():
    maze = solver.load_maze('maze3.txt')
    result = solver.solve(maze)
    assert result is True


def test_solve_maze4():
    maze = solver.load_maze('maze4.txt')
    result = solver.solve(maze)
    assert result is False
