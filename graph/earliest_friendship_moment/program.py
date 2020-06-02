""" 1101. The Earliest Moment When Everyone Become Friends

In a social group, there are N people, with unique integer ids from 0 to N-1.
We have a list of logs, where each logs[i] = [timestamp, id_A, id_B] contains a non-negative integer timestamp, and the ids of two different people.
Each log represents the time in which two different people became friends. 
Friendship is symmetric: if A is friends with B, then B is friends with A.
Let's say that person A is acquainted with person B if A is friends with B, or A is a friend of someone acquainted with B.
Return the earliest time for which every person became acquainted with every other person. Return -1 if there is no such earliest time.

Example 1:

Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
Output: 20190301
Explanation:
The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friend anything happens.
The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.

Note:

2 <= N <= 100
1 <= logs.length <= 10^4
0 <= logs[i][0] <= 10^9
0 <= logs[i][1], logs[i][2] <= N - 1
It's guaranteed that all timestamps in logs[i][0] are different.
logs are not necessarily ordered by some criteria.
logs[i][1] != logs[i][2]
"""


def earliestTimeAllFriend(N, timestamps):
    if N <= 1: return -1

    uf = UnionFindRank()
    earliest_time = timestamps[0][0]
    components = N

    timestamps.sort()

    for time, u, v in timestamps:
        if uf.connected(u, v): continue
        uf.union(u, v)
        components -= 1
        earliest_time = time

        if components == 1:
            return earliest_time

    return -1


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
