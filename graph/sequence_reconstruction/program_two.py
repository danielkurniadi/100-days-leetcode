""" 444. Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.

Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:
------------------
Input:
original: [1,2,3], sequences: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 3:
------------------
Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
------------------
Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true

Example 5:
------------------
Input:
org: [1,2,3,4], seqs: [[1,2],[2,3],[3,1],[3,4]]

Output:
false

Explanation:
There is backedge [3,1] which create cycle. This makes sequence infinitely
"""
from collections import defaultdict


# Approach 2: Using topological sorting
def sequenceReconTopo(original, sequences):
    """ Using Toposorting
    :type original list[int]
    :type sequences list[list[int]]
    :rtype bool
    """
    nodes = {node for seq in sequences for node in seq}
    graph = defaultdict(list)
    indegrees = {node: 0 for node in nodes}

    if len(nodes) != len(original):
        # False for lack or additional node in sequence not in original
        return False

    # build graph
    for sequence in sequences:
        for u, v in zip(sequence[:-1], sequence[1:]):
            graph[u].append(v)
            indegrees[v] += 1  # update in degree

    # build toposorting
    toposorted = []
    stack = [node for node in nodes
            if indegrees[node] == 0]

    # ensures only single unique path
    while len(stack)==1:
        node = stack.pop()
        toposorted.append(node)

        for neig in graph.get(node, []):
            indegrees[neig] -= 1
            if indegrees[neig] == 0:
                stack.append(neig)

    print(toposorted)
    return (toposorted == original)


if __name__ == '__main__':
    # TEST CASE 1
    original = [1,2,3]
    sequences = [[1,3],[1,2]]
    ans = sequenceReconTopo(original, sequences)
    print(ans)
