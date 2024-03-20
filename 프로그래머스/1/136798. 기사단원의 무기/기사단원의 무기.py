import math
def solution(number, limit, power):
    # 1부터 number까지 약수의 수를 구하고 더함
    # 그 약수의 수가 limit보다 크면 power를 더해야함
    answer = 0
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(math.sqrt(i) + 1)):
            if (i % j == 0):
                if(i / j == j):
                    count += 1
                else:
                    count += 2
        if count > limit:
            answer += power
        else:
            answer += count
    
    return answer