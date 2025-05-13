def solution(lines):
    line_1 = {i for i in range(lines[0][0], lines[0][1])}
    line_2 = {i for i in range(lines[1][0], lines[1][1])}
    line_3 = {i for i in range(lines[2][0], lines[2][1])}

    res = line_1 & line_2
    res = res | (line_2 & line_3)
    res = res | (line_1 & line_3)
    
    return len(res)
