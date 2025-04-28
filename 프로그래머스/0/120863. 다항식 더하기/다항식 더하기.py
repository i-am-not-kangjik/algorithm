def solution(polynomial):
    answer = ''
    x = 0
    num = 0
    
    polynomial = polynomial.split()
    
    for i in range(len(polynomial)):
        if polynomial[i] == '+':
            continue
        elif polynomial[i] == 'x':
            x += 1
        elif polynomial[i].isdigit():
            num += int(polynomial[i])
        else:
            x += int(polynomial[i][:-1])
            
    if x == 1:
        x = ''
    
    if x != 0:
        answer += f'{x}x'
    if x != 0 and num != 0:
        answer += f' + {num}'
    elif x == 0 and num != 0:
        return str(num)

    return answer