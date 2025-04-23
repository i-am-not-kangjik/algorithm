def solution(my_string):
    tmp = list(my_string.split(' '))
    answer = int(tmp.pop(0))
    
    for i in range(len(tmp)):
        if tmp[i].isdigit():
            if tmp[i - 1] == '+':
                answer += int(tmp[i])
            elif tmp[i - 1] == '-':
                answer -= int(tmp[i])
    
    return answer