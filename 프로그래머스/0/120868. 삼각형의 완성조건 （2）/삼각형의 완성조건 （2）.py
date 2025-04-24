def solution(sides):
    answer = 0
    
    # sides의 max보단 크고 sides의 합 보단 작은 개수
    # 3 + 6 > 7, 8
    
    for i in range(max(sides) + 1, sum(sides)):
        answer += 1
    
    for i in range(1, max(sides) + 1):
        if min(sides) + i > max(sides):
            answer += 1
    
    # + 
    
    # sides의 max가 가장 긴 변일 경우
    # 3 + x > 6 and x =< 6
    

    
    return answer