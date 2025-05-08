import math

def solution(a, b):
    
    gcd = math.gcd(a, b)
    
    if gcd != 1:
        b = int(b / gcd)
        a = int(a / gcd)
    

    while(b != 1):
        if b % 2 == 0:
            b = int(b / 2)
            continue
        elif b % 5 == 0:
            b = int(b / 5)
            continue
        elif b != 1:
            break
    
    return 1 if b == 1 else 2