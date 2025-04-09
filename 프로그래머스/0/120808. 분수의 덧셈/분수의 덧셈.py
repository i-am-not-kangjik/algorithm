def solution(numer1, denom1, numer2, denom2):
    # 분모 1이 분모 2보다 큰 경우 (분모 2가 항상 크게)
    if denom1 > denom2:
        numer1, denom1, numer2, denom2 = numer2, denom2, numer1, denom1
    
    
    # 분모2가 분모1의 배수일 경우
    if denom2 % denom1 == 0:
        tmp = denom2 // denom1
        denom1 *= tmp
        numer1 *= tmp
    else:
        i = 2
        while(denom1 * i % denom2 != 0):
            i += 1
        denom1 *= i
        numer1 *= i
        
        i = 2
        while(denom1 != denom2 * i):
            i += 1
        denom2 *= i
        numer2 *= i
    
    answer = []
    answer.append(numer1 + numer2)
    answer.append(denom1)
    
    if answer[0] == answer[1]:
        return[1, 1]
    
    for i in range(2, answer[1] + 1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer[0] /= i
            answer[1] /= i
    
    return answer