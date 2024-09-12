def solution(array):
    max = sorted(array)[-1]
    max_index = array.index(max)
    return [max, max_index]