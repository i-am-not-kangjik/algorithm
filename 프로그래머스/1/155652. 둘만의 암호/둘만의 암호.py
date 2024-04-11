def solution(s, skip, index):
    answer = ''
    skip_list = [ord(x) for x in skip]
    
    for i in s:
        tmp = ord(i)
        tmp_count = index
        while (tmp_count > 0):
            tmp += 1
            if tmp == 123:
                tmp = 97
            if tmp not in skip_list:
                tmp_count -= 1
        
        answer += chr(tmp)    
        
    return answer