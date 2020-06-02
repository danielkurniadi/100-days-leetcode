"""
"""


def find_longest_uncommon_subsequence(string_a, string_b):
    n = len(string_a)
    m = len(string_b)
    if string_a == string_b: return -1
    return max(len(string_a), len(string_b))


if __name__ == '__main__':
    string_a = "aefawfawfawfaw"
    string_b = "aefawfeawfwafwaef"
    ans = find_longest_uncommon_subsequence(string_a, string_b)
    print(ans)
