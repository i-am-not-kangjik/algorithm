def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        tmp = quiz[i].split('=')
        for j in range(len(tmp)):
            tmp[j] = tmp[j].strip()
        if str(eval(tmp[0])) == tmp[1]:
            answer.append('O')
        else:
            answer.append('X')
        
    return answer