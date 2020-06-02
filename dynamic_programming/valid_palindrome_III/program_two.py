from functools import lru_cache


def isValidPalindrome(s, k):

    @lru_cache(maxsize=None)
    def topDownDP(start, end, k):
        # return true when the left and right meet
        if start >= end:
            return True
        # when the edit quota is used up but the left and right have yet to 
        # meet, it means the string cannot be transformed into a valid 
        # palindrome with `k` deletions
        if k < 0:
            return False
        
        # when the start and end character matches
        if s[start] == s[end]:
            # check if the substring without the two ends can be transformed 
            # into a valid palindrome with the given `k`
            return topDownDP(start, end, k)
        
        return topDownDP(start+1, end, k-1) or topDownDP(start, end-1, k-1)
    
    return topDownDP(0, len(s)-1, k)


        