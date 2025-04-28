def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                if i != 0:
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                    if j != 0:
                        if board[i-1][j-1] != 1:
                            board[i-1][j-1] = 2
                    if j != len(board) - 1:
                        if board[i-1][j+1] != 1:
                            board[i-1][j+1] = 2
                
                if i != len(board) - 1:
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
                    if j != 0:
                        if board[i+1][j-1] != 1:
                            board[i+1][j-1] = 2
                    if j != len(board) - 1:
                        if board[i+1][j+1] != 1:
                            board[i+1][j+1] = 2
                
                if j != 0:
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                if j != len(board) - 1:
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2
                
    for i in board:
        answer += i.count(0)
    
    
    
    return answer