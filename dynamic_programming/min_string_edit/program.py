"""
"""
from functools import lru_cache


def debug(f):
    def top_down(p1, p2):
        ans = f(p1, p2)
        print(ans)
        return ans
    return top_down


def min_edit_distance(string1, string2):
    n = len(string1)
    m = len(string2)

    if n < m:
        string1, string2 = string2, string1
        n, m = m, n

    @lru_cache(maxsize=None)
    def topDown(p1, p2):
        if p2 == m:
            return n - p1

        elif p1 == n:
            return m - p2

        elif string1[p1] == string2[p2]:
            return topDown(p1+1, p2+1)

        else:
            return 1 + min(topDown(p1+1, p2+1),
                    topDown(p1, p2+1),
                    topDown(p1+1, p2))

    return topDown(0, 0)


if __name__ == "__main__":
    
    # EDGE CASE1
    string1, string2 = "", "ros"
    print(string1, string2, end=":")
    min_edit = min_edit_distance(string1, string2)
    print(min_edit)
    
    # EDGE CASE2
    string1, string2 = "ho", ""
    print(string1, string2, end=":")
    min_edit = min_edit_distance(string1, string2)
    print(min_edit)

    # TEST CASE1
    string1, string2 = "horse", "ros"
    print(string1, string2, end=":")
    min_edit = min_edit_distance(string1, string2)
    print(min_edit)

    # TEST CASE2
    string1, string2 = "roomba", "aloha"
    print(string1, string2, end=":")
    min_edit = min_edit_distance(string1, string2)
    print(min_edit)

    # TEST CASE3
    string1, string2 = "corona", "oreo"
    print(string1, string2, end=":")
    min_edit = min_edit_distance(string1, string2)
    print(min_edit)

    # TEST CASE4
    string1, string2 = "preparation", "participation"
    print(string1, string2, end=":")
    min_edit = min_edit_distance(string1, string2)
    print(min_edit)
