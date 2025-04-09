def solution(array):
    tmp = list(map(lambda x: str(x), array))
    return ''.join(tmp).count('7')