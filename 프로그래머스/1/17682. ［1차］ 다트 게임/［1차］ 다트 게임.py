def solution(dartResult): 
    # 숫자, 문자 분리해 담을 리스트
    dart = []
    
    # 두자리 숫자를 다루기 위한 문자열
    n = ''
    
    for item in dartResult:
        if item.isnumeric():
            n += item
        else:
            if n:
                dart.append(int(n))
                n = ''
            dart.append(item)

    # (S, D, T, *, #) 계산
    score = []
    
    i = 0
    while i < len(dart):
        d = dart[i]
        i += 1
        
        if (dart[i] == 'S'):
            score.append(d ** 1)
        elif (dart[i] == 'D'):
            score.append(d ** 2)
        elif (dart[i] == 'T'):
            score.append(d ** 3)
        i += 1
        
        if i < len(dart) and (dart[i] == '*' or dart[i] == '#'):
            if dart[i] == '*':
                score[-1] *= 2
                if len(score) > 1:
                    score[-2] *= 2
            elif dart[i] == '#':
                score[-1] *= -1
            i+=1
        
    return sum(score)

