""" Union Find Rank Implementation
"""


class Solution(object):
    def disjoint_network(self, m, n):
        """
        :type m: List[List][int]
        :type n: int
        :rtype: int
        """
        n_components = n
        uf = UnionFindRank()

        for i in range(n-1):
            for j in range(i, n):
                if m[i][j] > 2 and not uf.connected(i, j):
                    uf.union(i, j)
                    n_components -= 1
        return n_components


class UnionFindRank:
    """ Implementation of Union Find Rank with Path Compression
    """

    def __init__(self):
        self.parentsMap = {}
        self.ranksMap = {}

    def find(self, p):
        if not (p in self.parentsMap):
            self.parentsMap[p] = p
            self.ranksMap[p] = 1
            return p

        while p != self.parentsMap[p]:
            self.parentsMap[p] = self.parentsMap[self.parentsMap[p]]
            p = self.parentsMap[p]
        return p

    def connected(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        return (p_root == q_root)

    def union(self, p, q):
        p_root = self.parentsMap[p]
        q_root = self.parentsMap[q]

        if p_root == q_root: return

        p_rank, q_rank = self.ranksMap[p_root], self.ranksMap[q_root]

        if p_rank <= q_rank:
            self.parentsMap[p_root] = q_root
            self.ranksMap[q_root] += p_rank
        else:
            self.parentsMap[q_root] = p_root
            self.ranksMap[p_root] += q_rank


if __name__ == "__main__":
    solution = Solution()

    # TEST CASE 1:
    m = [[0, 3, 0],
        [3, 0, 0],
        [0, 0, 0]]
    n = 3
    ans = solution.disjoint_network(m, n)
    print("TestCase 1:", ans)

    # TEST CASE 2:
    m = [[0, 3, 0],
        [3, 0, 5],
        [0, 5, 0]]
    n = 3
    ans = solution.disjoint_network(m, n)
    print("TestCase 2:", ans)


    # TEST CASE 2:
    m = [[0, 3, 5],
        [3, 0, 5],
        [5, 5, 0]]
    n = 3
    ans = solution.disjoint_network(m, n)
    print("TestCase 3:", ans)
