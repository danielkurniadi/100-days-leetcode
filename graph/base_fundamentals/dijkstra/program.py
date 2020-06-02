""" Dijkstra Search on Directed Graph

Input:
T
V E
s t
u1 v1 w1 
u2 v2 w2
.
.
.

First line of input contains number of testcases T. For each testcase.
First line of each testcase contains number of nodes V and edges E, seperated by space
Second line of each testcase contain source node s and target node t in integer.
and next E lines contains triplets of integers: u v w; where u v w means an edge from u to v with weight w.

Output:
bool, dict

For each testcase, output whether we there is a path from node s to node t. Then output a dict that trace the shortest path.

Your task:
The task is to complete the function bfs() which should do the depth first traversal of given graph
and prints the node in BFS order.

Constraints:
1 <= T <= 100
2 <= V <= 200
1 <= E <= 200

Example:
Input:
1
5 6
2 1 100
1 0 90
1 3 80
0 4 200
3 4 300
2 3 50

Output:
True {4:3, 1:3}

Explanation:
Testcase 1: There is  one test cases.  
First line of each test case represent two integer V, E denoting number of vertices and edges
Second line of each testcase contain source node s and target node t in integer.
and then in each of the next E lines are triplets of values u, v, and w denotes there is a directed edge from u to v with weight w.

Then output True since there is a path from 1 to 4. And the dict output the trace: node 1 > node 3 > node 4 
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush

MAX_INT = 2**31


def dijkstra(graph, sourceNode, targetNode):
    queue = [(0, sourceNode)]
    seen = {sourceNode}
    dists, paths = {}, {}
    while queue:
        dist, currentNode = heappop(queue)
        seen.add(currentNode)

        if currentNode == targetNode:
            return True, paths

        for weight, neig in graph.get(currentNode, []):
            if neig in seen: continue
            alt = dist + weight
            if alt < dists.get(neig, MAX_INT):
                dists[neig] = alt
                heappush(queue, (alt, neig))
                paths[neig] = currentNode
    else:
        return False, paths


if __name__ == '__main__':
    # Driver code
    T = int(input().strip())  # number of test cases

    for _ in range(T):
        V, E = (int(x) for x in input().strip().split())  # number of vertices and edges
        sourceNode, targetNode = (int(x) for x in input().strip().split())

        # parse edges per line
        graph = defaultdict(list)
        for _ in range(E):
            u, v, w = (int(x) for x in input().strip().split())  # node U, node V, weight value
            graph[u].append((w, v))

        # run dijkstra
        found, paths = dijkstra(graph, sourceNode, targetNode)

        # display paths
        if found:
            currentNode = targetNode
            shortestpathOrdered = []
            while currentNode:
                shortestpathOrdered.append(currentNode)
                currentNode = paths.get(currentNode)
            shortestpathOrdered = shortestpathOrdered[::-1]

            print(" > ".join([str(x) for x in shortestpathOrdered]))
        else:
            print("Path from", sourceNode, "to", targetNode, "not found.")
