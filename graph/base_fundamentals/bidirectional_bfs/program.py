""" Bidrectional Breadth-first Search
Input:
T
V E
s t
u1 v1 u2 v2 ....

First line of input contains number of testcases T. For each testcase.
First line of each testcase contains number of nodes V and edges E, seperated by space
Second line of each testcase contain source node s and target node t in integer.
and next line contains E pairs of integers (u and v each) where u v means an edge from u to v.

Output:
For each testcase, print the nodes while doing BFS starting from node 0 in order-level manner.

Your task:
The task is to complete the function bfs() which should do the depth first traversal of given graph
and prints the node in BFS order.

Constraints:
1 <= T <= 100
1 <= V <= 200

Example:
Input:
1
16 17
1 14
0 4 1 4 2 5 3 5 4 6 5 6 6 7 7 8 8 9 9 11 9 12 8 10 10 13 10 14 6 19 19 20 20 8

Output:
1 4 6 7 8 10 14

Explanation:
Testcase 1: There is  one test cases.  
First line of each test case represent an integer N denoting number of edges
Second line of each testcase contain source node s and target node t in integer.
and then in the next line N pairs of values a and b are fed which denotes there is an edge from a to b.
"""

from collections import defaultdict, deque


def bidirectional_bfs(graph, sourceNode, targetNode):
    """
    :type graph: collections.defaultdict(list)
    :type sourceNode: int
    :type targetNode: int
    :rtype: (dict, dict, int)
    """
    seenOne, seenTwo = set(), set()
    parentsOne, parentsTwo = {}, {}
    queueOne, queueTwo = deque([sourceNode]), deque([targetNode])

    while queueOne and queueTwo:
        bfs_step(queueOne, graph, parentsOne, seenOne)
        bfs_step(queueTwo, graph, parentsTwo, seenTwo)

        intersectNodes = seenOne & seenTwo
        if intersectNodes:
            break
    
    return parentsOne, parentsTwo, list(intersectNodes)[0]


def bfs_step(queue, graph, parentsTrack={}, seen=set()):
    """
    :type queue: collections.deque
    :type graph: collections.defaultdict(list)
    :type parentsTrack: dict
    :type seen: set
    """
    if len(queue) > 0:
        currentNode = queue.popleft()

        for neig in graph.get(currentNode, []):
            if neig not in seen:
                queue.append(neig)
                parentsTrack[neig] = currentNode
                seen.add(neig)
    return


def print_path(parentsTrackOne, parentsTrackTwo, sourceNode, 
                targetNode, intersectionNode):
    """
    :type parentsTrackOne: dict
    :type parentsTrackTwo: dict
    :type intersectionNode: int
    """
    path = [intersectionNode]

    currentNode = intersectionNode
    while currentNode != sourceNode:
        parentNode = parentsTrackOne[currentNode]
        path.append(parentNode)
        currentNode = parentNode
    path = path[::-1]  # reverse path

    currentNode = intersectionNode
    while currentNode != targetNode:
        parentNode = parentsTrackTwo[currentNode]
        path.append(parentNode)
        currentNode = parentNode

    print("-" * len(parentsTrackOne) + "Path Tracing" + "-" * len(parentsTrackTwo))
    print(" > ".join(map(str, path)))

    return path


if __name__ == '__main__':
    # Driver code
    T = int(input().strip())

    for _ in range(T):
        V, E = (int(x) for x in input().strip().split())
        source, target = (int(x) for x in input().strip().split())
        edges = list(map(int, input().strip().split()))

        # build graph
        graph = defaultdict(list)
        for i in range(0, 2*E, 2):
            u, v = edges[i], edges[i+1]
            graph[u].append(v)
            graph[v].append(u)

        # bidirectional search
        parentsOne, parentsTwo, intersectionNode = bidirectional_bfs(graph, source, target)
        path = print_path(parentsOne, parentsTwo, source, target, intersectionNode)
