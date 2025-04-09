def solution(s):
    return ''.join(sorted(list(filter(lambda x: s.count(x) == 1, s))))