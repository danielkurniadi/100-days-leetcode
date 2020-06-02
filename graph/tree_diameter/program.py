"""
"""

from collections import defaultdict


def treeDiameter(edges):
    root = 0
    seen = set()

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def topDown(node, ancestor):
        seen.add(node)

        lengths = []
        max_length = 0

        for neig in graph.get(node, []):
            if neig in seen: continue
            child_length, prev_max = topDown(neig, ancestor+1)
            max_length = max(max_length, prev_max)
            lengths.append(child_length)

        right, left = 0, 0
        if len(lengths) == 0:
            right, left = 0, 0
        elif len(lengths) == 1:
            right, left = lengths[0], 0
        elif len(lengths) == 2:
            right, left = lengths

        print(node)
        print(max_length, right, left, ancestor)

        max_length = max(
            max_length,
            right + left,
            right + ancestor,
            left + ancestor
        )

        return max(right, left) + 1, max_length

    root = 0
    for node in graph:
        if len(graph[node]) == 1:
            root = node
            break

    print(root)
    _, max_length = topDown(root, 0)
    return max_length


if __name__ == "__main__":
    # TEST CASE 1
    edges = [[0,1],[0,2],[1,3],[0,4],[1,5],[2,6],[1,7]]
    diameter = treeDiameter(edges)
    print("Input:", edges)
    print("Output:", diameter)
