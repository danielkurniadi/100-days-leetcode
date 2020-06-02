"""
"""


def longest_palindrome_expand_centre(string):
    string = "#" + "#".join(string) + "#"
    n = len(string)

    table = [0] * n
    for i in range(1, n-1):
        l, r = i-1, i+1
        length = 0
        while 0 <= l and r < n:
            if string[l] == string[r]:
                length += 1
                l -= 1
                r += 1
            else: break
        table[i] = length

    length, center = max([(table[i], i) for i in range(1,n-1)])
    return string[center-length:center+length+1].replace("#", "")


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        string = input().strip()
        ans = longest_palindrome_expand_centre(string)
        print(ans)