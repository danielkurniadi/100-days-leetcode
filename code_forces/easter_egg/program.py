"""
"""

def easterEggColoring(n):
    fullcolor = ['R','O','Y','G','B','I','V']
    quadcolor = ['G','B','I','V']
    if n < 8:
        return "".join([fullcolor[i % 7] for i in range(n)])
    
    string = fullcolor
    string.extend([quadcolor[i % 4] for i in range(n-7)])
    return "".join(string)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        ans = easterEggColoring(n)
        print(ans)
