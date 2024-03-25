def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    while(A):
        if (len(A) > 1):
            if ((A[-1] * B[-1] + A[0] * B[0]) > (A[-1] * B[0] + B[-1] * A[0])):
                answer += (A.pop(0) * B.pop())
                answer += (B.pop(0) * A.pop())
            else:
                answer += (A.pop() * B.pop())
        else:
            answer += (A.pop() * B.pop())
    return answer  
