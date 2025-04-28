def solution(score):
    answer = [0] * len(score)
    tmp = [[sum(score[i]), i] for i in range(len(score))]
    
    tmp = sorted(tmp, reverse=True)
    
    
    rank = 1
    
    answer[tmp[0][1]] = 1
    for i in range (len(tmp) - 1):
        if tmp[i][0] == tmp[i+1][0]:
            answer[tmp[i][1]] = rank
            answer[tmp[i+1][1]] = rank
        else:
            answer[tmp[i][1]] = rank
            rank += answer.count(rank)

    answer[tmp[-1][1]] = rank
    
    return answer