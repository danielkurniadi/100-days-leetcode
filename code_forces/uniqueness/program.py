"""
"""


def deleteShortestSegmentToUniqueness(array):
    n = len(array)
    i, j = 0, n-1

    if len(array) == len(set(array)):
        return 0

    hashSet = set()
    while i < j:
        if not (array[i] in hashSet):
            hashSet.add(array[i])
            i += 1
        elif not (array[j] in hashSet):
            hashSet.add(array[j])
            j -= 1
        else:
            break

    return j - i + 1


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        array = list(map(int, input().strip().split()))
        ans = deleteShortestSegmentToUniqueness(array)
        print(ans)
