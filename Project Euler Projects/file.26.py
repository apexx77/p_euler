def task(n, d):
    for i in range(1, d):
        if 1 == 10 ** i % d:
            return i
    return 0
longest = max(task(1, i) for i in range(2, 1001))
print([i for i in range(2, 1001) if task(1, i) == longest][0])
