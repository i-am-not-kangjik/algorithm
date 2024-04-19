def solution(s):
    filtered_list = []
    n = ''
    for c in s:
        if c.isnumeric():
            n += c
        else:
            if n:
                filtered_list.append(int(n))
                n = ''
    unique_filtered_list = list(set(filtered_list))

    count_list = []
    for i in unique_filtered_list:
        count_list.append([i, filtered_list.count(i)])
    count_list.sort(key = lambda x : -x[1])
    return [x[0] for x in count_list]