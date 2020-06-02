# !/usr/bin/python3

"""
"""

def permute_numbers(nums):
    solutions = []

    # time complexity: O(N! . N)
    # space complexity: 
    #   + callstack from recursion --> O(N) space
    #   + remainings, results buffer --> O(N) space 
    #   + solutions --> O(N!)

    def recurse(remainings, results):
        if len(remainings) == 0:
            solutions.append(results[:])
            return

        for i, num in enumerate(remainings):
            # backtrack algorithm
            remainings.pop(i)  # O(N) hurting, TODO: optimise O(1) pop and insert back
            results.append(num)

            recurse(remainings, results)

            # reset the buffers
            remainings.insert(i, num)  # O(N) hurting, TODO: optimise
            results.pop()

    recurse(remainings=nums, results=[])
    return solutions
