def solution(my_str, n):
    # 몫
    mok = len(my_str) // n
    # 나머지
    nam = len(my_str) % n

    answer = []
    
    i = 0
    j = 0
    while(i < mok):
        answer.append(my_str[j:j+n])
        i += 1
        j += n
    
    if nam > 0:
        answer.append(my_str[-nam:])
    
    return answer