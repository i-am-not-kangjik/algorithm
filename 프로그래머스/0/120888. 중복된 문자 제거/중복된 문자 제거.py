def solution(my_string):
    tmp = [i for i in my_string]
    tmp2 = []
    for i in tmp:
        if i not in tmp2:
            tmp2.append(i)
    answer = "".join(tmp2)
    return answer