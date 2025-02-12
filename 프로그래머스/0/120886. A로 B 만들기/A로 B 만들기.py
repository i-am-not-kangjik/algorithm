def solution(before, after):
    before = sorted(list(before))
    after = sorted(list(after))
    
    return 1 if before == after else 0