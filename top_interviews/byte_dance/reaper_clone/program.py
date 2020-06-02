from collections import deque


def count_reaper(n):
    total_reaper = 1
    queue = deque([0])
    while queue:
        idx = queue.popleft()
        if idx < n-4:
            total_reaper += min(n-idx-4, 4)
            for i in range(idx+5, min(idx+9, n)):
                queue.append(i)
    return total_reaper



if __name__ == '__main__':
    ans = count_reaper(4)
    print("n:", 4, "ans", ans)

    ans = count_reaper(5)
    print("n:", 5, "ans", ans)

    ans = count_reaper(6)
    print("n:", 6, "ans", ans)

    ans = count_reaper(10)
    print("n:", 10, "ans", ans)

    ans = count_reaper(11)
    print("n:", 11, "ans", ans)

    ans = count_reaper(15)
    print("n:", 15, "ans", ans)
