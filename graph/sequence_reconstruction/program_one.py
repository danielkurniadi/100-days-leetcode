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

Example 2:
------------------
Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].

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
org: [1], seqs: [[1],[1],[1]]

Output:
true


Example 5:
------------------
Input:
org: [1], seqs: [[1],[2],[1]]

Output:
false

Example 6:
------------------
Input:
org: [1,2,3,4], seqs: [[1,2],[2,3],[3,1],[3,4]]

Output:
false

Explanation:
There is backedge [3,1] which create cycle. This makes sequence infinitely
"""

from collections import defaultdict


# Approach 1: Using UnionFind and many complicated checks
def sequenceReconNaive(original, sequences):
    """ Using Naive approach to check if sequence can be uniquely reconstructed
    :type: original: list[int]
    :type: sequences: list[list[int]]
    :rtype: bool

    Time Complexity: 
    + UnionFind all vertices: O( V log(V) )
    + DFS: O( V+E ); where E here are edges from parsing pair in sequences

    Keypoint/Ideas: 
        1. We build a graph by traversing each sequences. One node to other in the sequence act as edges.
        2. Lastly, we dfs the graph from the head (1st element of original) and check if any path lead to same sequence as original.

    There are 3 points to check
        1. Verify only int/node in original exists in each sequences, else return False
        2. Traverse the graph in dfs manner while track the path. There should exist a path that is equal to original sequence
        3. Check no cycle at all in the graph.
    """
    if len(original) == 0 or len(sequences) == 0:
        return False

    graph = defaultdict(set)
    orgSet = set(original)

    for sequence in sequences:
        if len(sequence) == 1:
            u = sequence[0]

            # check only node in original exists
            if u not in orgSet:
                return False
            graph[u]  # standalone node
            continue

        for u, v in zip(sequence[:-1], sequence[1:]):

            # check only node in original exits
            if not (u in orgSet and v in orgSet):
                return False
            graph[u].append(v)  # build graph

    if original[0] not in graph:
        # head component missing from sequence
        return False

    noCycle = True
    def dfs(node, idx, recStack):
        nonlocal graph, original, noCycle

        # check if this path still match element in original
        if idx >=  or node != original[idx]:
            return False

        recStack.add(node)  # mark as gray node

        neighbours = graph.get(node, [])
        if len(neighbours) == 0 and idx == len(original) - 1:
            # reached end of path matching with original
            return True

        for neig in neighbours:
            if not (neig in recStack):
                if dfs(neig, idx+1, recStack):
                    return True
            else:
                # cycle detected
                noCycle = False
                return False
        return False

    # run dfs
    return dfs(original[0], idx=0, recStack=set()) and noCycle
    
