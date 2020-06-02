"""
"""

from collections import Counter


def subarray_with_k_different(nums, k):
    print("-" * 25)
    N = len(nums)
    p1, p2 = 0, -1

    counter = Counter()
    numSet = set()

    answer = 0

    for p3 in range(N):
        num = nums[p3]
        
        counter[num] += 1
        numSet.add(num)

        if len(numSet) == k and p2 == -1:
            p2 = p3
        
        while len(numSet) > k:
            while p1 < p2:
                for i in range(p2, p3):
                    print("result:", nums[p1:i+1])
                answer += p3 - p2
                rnum = nums[p1]
                counter[rnum] -= 1
                if counter[rnum] == 0:
                    numSet.remove(rnum)
                p1 += 1
            p2 += 1

    while p2 < N:
        while len(numSet) == k and p1 < p2:
            for i in range(p2, N):
                print("result:", nums[p1:i+1])
            answer += N - p2
            rnum = nums[p1]
            counter[rnum] -= 1
            if counter[rnum] == 0:
                numSet.remove(rnum)
            p1 += 1
        p2 += 1

    return answer + (0 if k > 1 else N)


if __name__ == '__main__':
    # EDGE CASE
    nums = [1, 1, 1, 1, 1]
    ans = subarray_with_k_different(nums, k=1)
    print("Total subarray", ans)

    # TEST CASE 1
    nums = [1, 1, 2, 1, 2, 3, 2]
    ans = subarray_with_k_different(nums, k=2)
    print("Total subarray:", ans)

    # TEST CASE 2
    nums = [1, 2, 1, 3, 4]
    ans = subarray_with_k_different(nums, k=4)
    print("Total subarray:", ans)

    # TEST CASE 3
    nums = [1, 2, 1, 2, 3]
    ans = subarray_with_k_different(nums, k=2)
    print("Total subarray", ans)

    # TEST CASE 3
    nums = [1, 2, 1, 2, 3, 1]
    ans = subarray_with_k_different(nums, k=3)
    print("Total subarray", ans)