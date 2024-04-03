def solution(want, number, discount):
    answer = 0
    
    for i in range(0, len(discount) - 9):
        tmp = discount[i:i+10]
        isGood = True
        for j in range(0, len(want)):
            if tmp.count(want[j]) != number[j]:
                isGood = False
                break
        if isGood:
            answer += 1
    return answer