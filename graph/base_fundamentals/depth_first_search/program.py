"""Input:
First line of input contains number of testcases T. For each testcase.
First line of each testcase contains number of nodes and edges seperated by space
and next line contains N pairs of integers (X and Y each) where X Y means an edge from X to Y.

Output:
For each testcase, print the nodes while doing DFS starting from node 0 in pre-order manner.

Your task:
The task is to complete the function dfs() which should do the depth first traversal of given graph
and prints the node in DFS order.

Constraints:
1 <= T <= 100
1 <= N <= 200

Example:
Input:
2
5 4
0 1 0 2 0 3 2 4
4 3
0 1 1 2 0 3

Output:
0 1 2 4 3    // dfs from node 0
0 1 2 3

Explanation:
Testcase 1: There is  one test cases.  
First line of each test case represent an integer N denoting number of edges
and then in the next line N pairs of values a and b are fed which denotes there is an edge from a to b.
"""

from collections import defaultdict


def dfs(graph, sourceNode):
    """
    :type graph: defaultdict
    :type sourceNode: int
    :rtype: list[int]
    """
    # iterative solution
    traverseOrder = []
    stack = [sourceNode]
    seen = set()
    while stack:
        currentNode = stack.pop()
        if currentNode in seen: continue

        traverseOrder.append(currentNode)
        seen.add(currentNode)

        for neig in reversed(graph.get(currentNode, [])):
            if neig in seen: continue
            stack.append(neig)
    
    return traverseOrder


if __name__ == '__main__':
    # driver code
    T = int(input().strip())    
    for _ in range(T):
        V, E = (int(x) for x in input().strip().split())
        edges = list(map(int, input().strip().split()))    
        graph = defaultdict(list)  # directed graph
        for i in range(0, 2*E, 2):
            u, v = edges[i], edges[i+1]
            graph[u].append(v)
        traverseOrder = dfs(graph, 0)  # source is node 0
        print(traverseOrder)
