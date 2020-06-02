from collections import deque


def isValidPalindrome(s, k):
    """ Valid palindrome
    :type: s: str
    :type: k: int
    """
    n = len(s)
    if n <=1: return True
    
    def check_palindrome(bitmask):
        i, j = 0, n-1
        while i < j:
            bi = 1 << i
            bj = 1 << j
            if bi & bitmask:
                i += 1; continue
            if bj & bitmask:
                j -= 1; continue
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True

    # run brute search
    queue = deque([0])
    count = 0

    while queue and count <= k:
        for _ in range(len(queue)):
            bitmask = queue.popleft()
            if check_palindrome(bitmask):
                return True
            for i in range(n):
                b = 1 << i
                if not b & bitmask:
                    queue.append(bitmask ^ b)
        count += 1
    return False
