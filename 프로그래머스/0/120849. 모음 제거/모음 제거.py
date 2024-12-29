def solution(my_string):
    tmp = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in my_string:
        if i not in tmp:
            answer += i
    return answer