def solution(arr):
    answer = arr
    
    len_w = len(arr[0])
    len_h = len(arr)
    
    if len_w > len_h:
        for i in range(len_w - len_h):
            answer.append([0 for j in range(len_w)])
    elif len_h > len_w:
        for i in range(len_h):
            for j in range(len_h - len_w):
                answer[i].append(0)
    
    return answer