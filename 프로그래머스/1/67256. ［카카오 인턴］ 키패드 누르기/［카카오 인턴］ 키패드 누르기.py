def find_index(matrix, target):
    for row_index, row in enumerate(matrix):
        if target in row:
            col_index = row.index(target)
            return [row_index, col_index]

def solution(numbers, hand):
    keypad = [['*', 0, '#'], [7, 8, 9], [4, 5, 6], [1, 2, 3]]
    l = [0, 0]
    r = [0, 2]
    answer = ''
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            l = find_index(keypad, i)
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            r = find_index(keypad, i)
        else:
            target_index = find_index(keypad, i)
            l_distance = abs(l[0] - target_index[0]) + abs(l[1] - target_index[1])
            r_distance = abs(r[0] - target_index[0]) + abs(r[1] - target_index[1])
            if (l_distance < r_distance):
                answer += 'L'
                l = target_index
            elif (r_distance < l_distance):
                answer += 'R'
                r = target_index
            else:
                if hand == 'left':
                    answer += 'L'
                    l = target_index
                else:
                    answer += 'R'
                    r = target_index
    return answer