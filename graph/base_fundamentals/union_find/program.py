""" Union Find Rank Implementation
"""


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