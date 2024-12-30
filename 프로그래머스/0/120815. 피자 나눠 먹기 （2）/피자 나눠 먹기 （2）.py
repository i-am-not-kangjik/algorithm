def solution(n):
    pizza = 6
    answer = 1

    while pizza % n != 0:
        pizza += 6
        answer += 1
        
    return answer