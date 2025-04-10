def solution(array):
    count_array = [0] * 1000
    for i in range(len(array)):
        if count_array[array[i]] == 0:
            count_array[array[i]] = array.count(array[i])
    
    tmp = sorted(count_array)
    
    if tmp[-1] == tmp[-2]:
        return -1
    else:
        return count_array.index(tmp[-1])
    