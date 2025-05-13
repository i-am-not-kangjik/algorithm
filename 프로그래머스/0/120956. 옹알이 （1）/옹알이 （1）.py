def solution(babbling):
    answer = 0
    items = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        for j in items:
            babbling[i] = babbling[i].replace(j, '*', 1)

    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace('*', '')
        if babbling[i] == '':
            answer += 1
    
    
    
    return answer