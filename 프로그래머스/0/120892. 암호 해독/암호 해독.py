def solution(cipher, code):
    answer = ''
    for i in range(1, len(cipher)):
        if (i % code == 0):
            answer += cipher[i-1]
    if (len(cipher) % code == 0):
        answer += cipher[-1]
    return answer