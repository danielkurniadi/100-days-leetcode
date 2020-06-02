"""
"""

def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = array[l:m+1]
    R = array[m+1:r+1]

    i, j, k = 0, 0, l

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        array[k] = i
        k, i = k + 1, i + 1
    while j < len(R):
        array[k] = j
        k, j = k + 1, j + 1
    return array


def merge_sort(array, l=0, r=None):
    if r is None:
        r = len(array) - 1
    if l < r:
        m = (l + r) // 2
        merge_sort(array, l, m)
        merge_sort(array, m+1, r)
        merge(array, l, m, r)
    return array
