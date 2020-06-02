""" A Strange Sorting Problem

Due to a bug in trading program ...
"""

from functools import lru_cache


def strangeSort(numstrs, mapping):
    @lru_cache(maxsize=None)
    def convert_to_correct(numstr):
        """ Convert numeric string to int. Assuming correct numeric string (no check)
        :type numstr: str
        :type mapping: List[int]
        :rtype: List[str]
        """
        correct_num = 0
        neg = 1
        for c in numstr:
            if c == '-':
                neg = -1
                continue
            correct_num += correct_num * 10 + mapping[int(c)]
        return neg * correct_num

    mapping = {mapping[idx]: idx for idx in range(10)}
    correct_nums = [(convert_to_correct(numstr), i)
                    for i, numstr in enumerate(numstrs)]  # List[int]
    correct_nums.sort()

    order_numstr = [numstrs[i] for num, i in correct_nums]
    return order_numstr


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        numstrs = input().strip().split()
        mapping = list(map(int, input().strip().split()))
        assert len(mapping) == 10

        print("-" * 50)
        print("Input Num:", numstrs)
        print("Input Map:", mapping)

        ans = strangeSort(numstrs, mapping)
        print(ans, '\n')
