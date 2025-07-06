def get_cross(line1, line2):
    bf = line1[1] * line2[2]
    ed = line1[2] * line2[1]
    ad = line1[0] * line2[1]
    bc = line1[1] * line2[0]
    ec = line1[2] * line2[0]
    af = line1[0] * line2[2]

    if ad - bc == 0:
        return False
    
    x = (bf - ed) / (ad - bc)
    y = (ec - af) / (ad - bc)
    
    if x == int(x) and y == int(y):
        return [int(x), int(y)]
    else:
        return False

def solution(line):
    tmp = []
    
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            res = get_cross(line[i], line[j])
            if res != False and res not in tmp:
                tmp.append(res)
                
    tmp = sorted(tmp)

    min_x = tmp[0][0]
    max_x = tmp[-1][0]
    
    tmp = sorted(tmp, key = lambda x : x[-1])
    min_y = tmp[0][1]
    max_y = tmp[-1][1]
    
    answer = []
    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    for i in range(height):
        answer.append(['.' for _ in range(width)])
    
    for x, y in tmp:
        star_x = x - min_x
        star_y = max_y - y
        answer[star_y][star_x] = '*'
    
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    
    return answer