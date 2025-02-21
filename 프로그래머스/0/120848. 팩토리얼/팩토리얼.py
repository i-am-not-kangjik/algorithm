def solution(n):
    answer = 1
    
    for i in range(2, 11):
        if answer * (i) <= n:
            answer *= i
        else:
            return i - 1
    
    return 10