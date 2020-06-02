"""
"""


def longest_palindrome_brute(string):
    string = "#".join(string)
    n = len(string)

    def check_palindrome(i, j):
        while i <= j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True

    longest_palindrome = ""
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if check_palindrome(i, j):
                # print(string[i:j+1])
                if len(longest_palindrome) < j-i+1:
                    longest_palindrome = string[i:j+1]

    return longest_palindrome.replace("#","")


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        string = input().strip()
        ans = longest_palindrome_brute(string)
        print(ans)
