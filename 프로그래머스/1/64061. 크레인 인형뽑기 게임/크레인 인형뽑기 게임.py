import numpy as np

def solution(board, moves):
    result = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0 and board[i][move-1] != 'X':
                result.append(board[i][move-1])
                board[i][move-1] = 'X'
                if len(result) > 1 and result[-1] == result[-2]:
                    answer += 2
                    result.pop()
                    result.pop()
                break
        
    return answer

# 4 1 2 5 4 1 5 4 3

# 복숭아 공룡 고양이 고양이 공룡 무지 복숭아