"""
Consider an M × N grid graph. The vertices in the grid graph are identified by its row and column number, i.e., for a vertex, 
there are two numbers (i, j) associated with it, where 1 ≤ i ≤ M is its row, and 1 ≤ j ≤ N is its column.
There is a thief in the grid at location (X, Y) and a cop at (X1, Y1).
There is a list C, which contains cell coordinates that are blocked for the cop to enter.
From a given cell (i, j) the cop can go to one of the four neighbor cells {up, down, right, left} in unit time.
How fast can the police reach the thief?

Output:
A single integer which tells minimum time it takes for the cop to reach the thief.
If the cop cannot reach the theif forever, output -1.
"""
from heapq import heappop, heappush
MAX_INT = 2 ** 32


def find_thief(M, N, x1, y1, x2, y2, C):
    cops = x2, y2
    thief = x1, y1
    obstacles = set(C)

    if (cops in obstacles) or (thief in obstacles):
        return -1

    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    queue = [(0, cops)]
    visited = set()
    dists = {}
    
    while queue:
        dist, cell = heappop(queue)
        visited.add(cell)

        if cell == thief:
            return dist
        
        x, y = cell

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (nx, ny) in visited or (nx, ny) in obstacles:
                continue
            if 1 <= nx <= M and 1 <= ny <= N:
                alt_dist = dist + 1
                if alt_dist < dists.get((nx, ny), MAX_INT):
                    dists[(nx, ny)] = alt_dist
                    heappush(queue, (alt_dist, (nx, ny)))
    else:
        return -1


if __name__ == "__main__":
    # TEST CASE 1
    test = [4, 4, 1, 1, 3, 3, []]
    answ = find_thief(*test)
    print(answ)

    # TEST CASE 2
    test = [4, 4, 2, 2, 3, 3, [(2,3),(3,2),(3,4)]]
    answ = find_thief(*test)
    print(answ)

    # TEST CASE 2
    test = [4, 4, 1, 1, 1, 1, [(2, 3), (3, 2)]]
    answ = find_thief(*test)
    print(answ)

    # TEST CASE 3
    test = [4, 4, 1, 1, 3, 3, [(1, 1), (3, 2)]]
    answ = find_thief(*test)
    print(answ)
