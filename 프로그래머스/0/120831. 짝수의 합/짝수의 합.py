def solution(n):
    count = 0
    n = n if n % 2 == 0 else n - 1
    for i in range (2, n + 1):
        if i % 2 == 0:
            count += i
    return count
