""" 1102. Path With Maximum Minimum Value
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.
A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

Input 
A: [
    [3,4,6,3,4],
    [0,2,1,1,7],
    [8,8,3,2,7],
    [3,2,4,9,8],
    [4,1,2,0,0],
    [4,6,5,4,3]
]
Output: 3

Note:

-- 1 <= R, C <= 100
-- 0 <= A[i][j] <= 10^9
"""

from heapq import heappop, heappush

class Solution:

    # Approach 1: Using Dijkstra with Min value of path as "distance"
    def maximumMinimumPath(self, A):
        """ Find Maximum of MinPath in Grid
        :type A: list[list[int]]: 2D Matrix
        :rtype: int: maximum value possible of min path
        """
        N, M = len(A), len(A[0])

        maxheap = [(-A[0][0], 0, 0)]
        visited = [[False for x in range(M)] for y in range(N)]

        while len(maxheap) > 0:
            value, i, j = heappop(maxheap)
            if i == N-1 and j == M-1:
                return -value
            if visited[i][j]: continue
            visited[i][j] = True
            for ni, nj in [(ni+1,nj),(ni,nj+1),(ni-1,nj),(ni,nj-1)]:
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                    alt = max(value, -A[ni][nj])
                    heappush(maxheap, (alt, ni, nj))
        return "notfound"
