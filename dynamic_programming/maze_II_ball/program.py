"""
"""
from functools import lru_cache
from heapq import heapify, heappop, heappush

MAX_INT = 2**31


def find_shortest_way(maze, ball, hole):
    N = len(maze)
    M = len(maze[0])

    def roll_ball(direction, ball):
        dy, dx = direction
        y, x = ball

        dist = 0
        while 0 <= x + dx < M and 0 <= y + dy < N:
            if (y, x) == hole: break
            if maze[y+dy][x+dx] == 1: break

            x, y = x + dx, y + dy
            dist += 1
        return (y, x), dist

    directions = {
        'l': (0,-1),
        'r': (0,1),
        'd': (1,0),
        'u': (-1,0)
    }

    def dijkstra(src, dest):
        queue = [(0, "", src)]
        seen = {src}
        dists = {}

        while queue:
            dist, path, cell = heappop(queue)
            seen.add(cell)

            if cell == dest:
                return True, path

            for direction in directions:
                dy, dx = directions[direction]
                next_cell, add_dist = roll_ball((dy, dx), cell)
                print(direction, next_cell)

                if next_cell in seen: continue

                alt = dist + add_dist
                if alt < dists.get(next_cell, MAX_INT):
                    dists[cell] = alt
                    heappush(queue, (alt, path + direction, next_cell))

        else:
            return False, ""
    
    return dijkstra(ball, hole)


if __name__ == '__main__':
    maze = [[0,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,0,0],
            [0,1,0,0,1],
            [0,1,0,0,0]]
    ball = (4,3)
    hole = (0,1)

    found, path = find_shortest_way(maze, ball, hole)
    print("Output: ", found, path)
