"""
"""

from functools import lru_cache


def can_frog_cross(stones):
    stones.sort()
    stones_set = set(stones)

    @lru_cache(maxsize=None)
    def top_down(i, jump):
        if i == stones[-1]: return True
        if i not in stones_set: return False

        if jump == 1:
            # if jump is only one, frog has no choice but jump forward
            # with jump+1 / jump stones ahead
            return top_down(i+jump+1, jump+1) or top_down(i+jump, jump)

        # jump to either jump+1 / jump / jump-1 stones ahead
        return top_down(i+jump+1, jump+1) or top_down(i+jump, jump) or top_down(i+jump-1, jump-1)

    return top_down(stones[0]+1, 1)


if __name__ == "__main__":
    # TEST CASE 1
    stones = [0,1,3,5,6,8,12,17]
    success = can_frog_cross(stones)
    print(success)

    # TEST CASE 2
    stones = [0,1,2,3,4,8,9,11]
    success = can_frog_cross(stones)
    print(success)
