def solution(my_string):
    answer = 0
    tmp = ''
    
    for i in range(len(my_string)):
        if i < len(my_string) - 1:
            if my_string[i].isnumeric():
                if my_string[i+1].isnumeric():
                    tmp += my_string[i]
                else:
                    if tmp:
                        tmp += my_string[i]
                        answer += int(tmp)
                        tmp = ''
                    else:
                        answer += int(my_string[i])
        if i == len(my_string) - 1:
            if my_string[i].isnumeric():
                if tmp:
                        tmp += my_string[i]
                        answer += int(tmp)
                        tmp = ''
                else:
                    answer += int(my_string[i])
    return answer