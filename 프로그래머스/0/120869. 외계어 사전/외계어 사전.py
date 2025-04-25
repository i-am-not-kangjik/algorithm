def solution(spell, dic):
    spell.sort()
    
    for i in dic:
        if len(i) != len(spell):
            continue
        else:
            if sorted(i) == spell:
                return 1
    return 2