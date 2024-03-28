def solution(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    
    return len(s1_set & s2_set)