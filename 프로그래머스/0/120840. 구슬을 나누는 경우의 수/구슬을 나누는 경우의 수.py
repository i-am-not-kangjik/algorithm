def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

def solution(balls, share):
    return factorial(balls) / (factorial(balls - share) * factorial(share))