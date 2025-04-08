def solution(array, n):
    array = sorted(array)
    
    # n과의 거리를 담은 배열
    tmp_array = [abs(n - i) for i in array]    
    
    # n과의 거리가 제일 가까운 수
    min_tmp_array = min(tmp_array)
    
    
    # n과의 거리가 제일 가까운 수가 한개일 때
    if tmp_array.count(min_tmp_array) == 1:
        return array[tmp_array.index(min_tmp_array)]
    else:
        # n과의 거리가 제일 가까운 수들의 index를 저장하는 배열
        tmp2_array = []
        for i in range(len(tmp_array)):
            if tmp_array[i] == min_tmp_array:
                tmp2_array.append(i)
        return(array[tmp2_array[0]])
    return array[tmp_array.index(min_tmp_array)]