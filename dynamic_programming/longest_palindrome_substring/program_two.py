"""
"""
from functools import lru_cache


def longest_palindrome_dp(string):
    if len(string) == 1:
        return string

    string = "#" + "#".join(string) + "#"
    n = len(string)

    @lru_cache(maxsize=None)
    def check_palindrome(i, j):
        if i >= j: return True
        return (string[i] == string[j]) and check_palindrome(i+1, j-1)

    l, r = 0, 0
    for i in range(1,n-1):
        for j in range(n-1, i, -1):
            if check_palindrome(i, j) and  r-l < j-i:
                l, r = (i, j)

    return string[l:r+1].replace("#", "")


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        string = input().strip()
        ans = longest_palindrome_dp(string)
        print(ans)

        