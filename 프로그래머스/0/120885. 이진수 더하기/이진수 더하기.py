def solution(bin1, bin2):
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    
    answer = ''
    answer += bin(bin1 + bin2)
    return answer[2:]