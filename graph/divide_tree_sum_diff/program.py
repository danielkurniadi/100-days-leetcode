""" Divide Tree into Two with Min Tree Sum Diff
Input:
First line of input contains number of testcases T. For each testcase.
First line of each testcase contains number of nodes and edges seperated by space
and next line contains E pairs of integers (X and Y each) where X Y means an edge from X to Y
and the next line contain V integers denoteing values for corresponding nodes.

Output:
For each testcase, print the nodes while doing BFS starting from node 0 in order-level manner.

Your task:
Given an undirected tree with V nodes and E edges whose each node is associated with a value.
We need to delete one edge to deivide tree into two subtrees such that 
the difference between sum of value in one subtree to sum of weight in other subtree is minimized.

Constraints:
1 <= T <= 100
2 <= V <= 200;
1 <= E <= 200
each node labelles from 0 <= v <= V-1
"""

from collections import defaultdict

MAX_INT = 2**31


def delete_edge_min_sum_diff(rootNode, tree, nodeVals):
    """
    :type rootNode: int
    :type tree: defaultdict(list)
    :type nodeVals: list[int]
    """
    def dfs_sum_tree(node, sum_cache):
        children = tree.get(node, [])
        sumChildren = 0
        if len(children) > 0:
            sumChildren = sum([dfs_sum_tree(child, sum_cache) for child in children])
        
        totalSum = sumChildren + nodeVals[node]
        sum_cache[node] = totalSum
        return totalSum
    
    def dfs_split_tree(node, sum_cache, totalSum):
        minSumDiff, edgeDeleted = MAX_INT, (None, None)
        children = tree.get(node, [])
        sumSubtrees = [sum_cache[child] for child in children]

        for child in children:
            sumDiff, childEdgeDel = dfs_split_tree(child, sum_cache, totalSum)
            if sumDiff < minSumDiff:
                minSumDiff, edgeDeleted = sumDiff, childEdgeDel

        for idx, sumSubtree in enumerate(sumSubtrees):
            sumDiff = totalSum - sumSubtree
            if sumDiff < minSumDiff:
                minSumDiff = sumDiff
                edgeDeleted = (node, children[idx])
        return minSumDiff, edgeDeleted

    # get sum for each tree, save in cache
    sum_cache = {}
    totalSum = dfs_sum_tree(rootNode, sum_cache)

    # brute force split tree into two by deleting an edge
    # then check if two subtree has min abs sum diff
    minDiffSum, edgeDeleted = dfs_split_tree(rootNode, sum_cache, totalSum)

    return minDiffSum, edgeDeleted


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        V, E = (int(x) for x in input().strip().split())
        edges = list(map(int, input().strip().split()))
        nodeVals = list(map(int, input().strip().split()))

        # build tree
        tree = defaultdict(list)
        for i in range(0, 2*E, 2):
            u, v = edges[i], edges[i+1]
            tree[u].append(v)

        rootNode = edges[0] if len(edges) > 0 else 0
        minSumDiff, edgeDeleted = delete_edge_min_sum_diff(rootNode, tree, nodeVals)

        print("Delete Edge:", edgeDeleted)
        print("Sum Difference:", minSumDiff)
