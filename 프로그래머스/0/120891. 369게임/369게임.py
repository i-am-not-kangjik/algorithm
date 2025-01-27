import re

def solution(order):
    answer = re.findall(r'[369]', str(order))
    return len(answer)