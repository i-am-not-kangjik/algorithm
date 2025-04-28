def solution(chicken):
    answer = 0
    
    while (chicken > 9):
        answer += chicken // 10
        res = chicken % 10
        chicken //= 10
        chicken += res
    
    return answer