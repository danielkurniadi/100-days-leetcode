"""
"""


def analyse_investment(investring):
    n = len(investring)
    investring = investring.upper()

    ans = 0
    
    counter = {'A': 0, 'B': 0, 'C': 0}
    total_count = 0

    l, r = 0, 0
    
    while l < n:
        while r < n:
            char = investring[r]
            
            if char in counter:
                counter[char] += 1
                if counter[char] <= 1:
                    total_count += 1

            if total_count == 3:
                break

            r += 1

        if total_count == 3:
            while total_count == 3:
                for j in range(r, n):
                    print(investring[l:j+1])
                ans += n - r
                char = investring[l]
                if char in counter:     
                    counter[char] -= 1
                    
                    if counter[char] < 1:
                        total_count -= 1
                l += 1
            r += 1
        else:
            l += 1

    return ans


if __name__ == '__main__':
    # TEST CASE 1
    investring = "ABBCZBAC"
    ans = analyse_investment(investring)
    print(ans, '\n')
    
    # TEST CASE 2
    investring = "ABCCBA"
    ans = analyse_investment(investring)
    print(ans, '\n')
    
    # TEST CASE 3
    investring = "ABCC"
    ans = analyse_investment(investring)
    print(ans, '\n')