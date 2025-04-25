def solution(keyinput, board):
    garo = board[0] // 2
    sero = board[1] // 2

    answer = [0, 0]
    for i in keyinput:
        if i == 'left' and answer[0] != garo * -1:
            answer[0] -= 1
        if i == 'right' and answer[0] != garo:
            answer[0] += 1
        if i == 'up' and answer[1] != sero:
            answer[1] += 1
        if i == 'down' and answer[1] != sero * -1:
            answer[1] -= 1
    return answer