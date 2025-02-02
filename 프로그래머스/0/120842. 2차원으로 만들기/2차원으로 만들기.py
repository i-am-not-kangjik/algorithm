def solution(num_list, n):
    tmp = len(num_list) // n
    answer = []
    for i in range(tmp):
        answer.append(num_list[:n])
        num_list = num_list[n:]
    return answer