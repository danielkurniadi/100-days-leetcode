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

class Solution:
    @staticmethod
    def find(p, unionset, unionrank):
        if p not in unionset:
            unionrank[p] = p
            unionrank[p] = 1
            return p
        while p != unionset[p]:
            # path compression
            unionset[p] = unionset[unionset[p]]
            p = unionset[p]
        return p

    @staticmethod
    def union(p, q, unionset, unionrank):
        p_root = Solution.find(p, unionset, unionrank)
        q_root = Solution.find(q, unionset, unionrank)

        if p_root == q_root:
            return

        p_rank = unionrank[p_root]
        q_rank = unionrank[q_root]

        if p_rank <= q_rank:
            unionset[p_root] = q_root
            unionrank[q_root] += p_rank
        else:
            unionset[q_root] = p_root
            unionrank[p_root] += q_rank

    # Approach 1: Using Dijkstra with Min value of path as "distance"
    def maximumMinimumPath(self, A):
        """ Find Maximum of MinPath in Grid
        :type A: list[list[int]]: 2D Matrix
        :rtype: int: maximum value possible of min path
        """
        N, M = len(A), len(A[0])
        unionset, unionrank = {}, {}
        nums = [(A[i][j], i, j) for i in range(N) for j in range(M)]
        nums.sort()

        res = A[0][0]
        while nums:
            value, i, j = nums.pop()
            unionset[(i,j)] = (i, j)
            unionrank[(i,j)] = 1
            res = min(res, value)

            for ni, nj in [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]:
                if (ni,nj) in unionset:
                    self.union((i,j), (ni,nj), unionset, unionrank)
            
            if self.find((0,0), unionset, unionrank) == \
                self.find((N-1,M-1), unionset, unionrank):
                return res

