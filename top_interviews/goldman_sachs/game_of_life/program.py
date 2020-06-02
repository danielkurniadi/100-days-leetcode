"""
"""
import pprint


def game_of_life(grid, rule, turn):
    n, m = len(grid), len(grid[0])
    
    directions = [(di, dj)
                  for di in range(-1,2)
                  for dj in range(-1,2)
                  if not (di == 0 and dj == 0)]

    for k in range(turn):
        new_grid = [[0 for _ in range(m)]
                    for _ in range(n)]
        for i in range(n):
            for j in range(m):
                neighbours_count = 0

                for di, dj in directions:
                    nxti, nxtj = i + di, j + dj
                    
                    if not (0 <= nxti < n and 0 <= nxtj < m):
                        continue
                    
                    if grid[nxti][nxtj] == 1:
                        neighbours_count += 1

                new_grid[i][j] = 1 if rule[neighbours_count] else 0
                # else: # TODO: turn of in goldman sachs
                #     new_grid[i][j] = 1 if neighbours_count == 3 else 0

    return new_grid


if __name__ == '__main__':
    turn = 1
    rule = [0, 0, 1, 1, 0, 0, 0, 0, 0]
    
    # TEST CASE 1
    grid = [[0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]]
    next_grid = game_of_life(grid, rule=rule, turn=turn)
    pprint.pprint(next_grid)


    # TEST CASE 2
    turn = 1
    rule = [0, 1, 0, 0, 0, 0, 0, 0, 0]
    grid = [[0, 1, 0, 0],
            [0, 0, 0, 0]]
    next_grid = game_of_life(grid, rule=rule, turn=turn)
    pprint.pprint(next_grid)