def solution(num, total):
    # 첫 번째 숫자 계산: (total - (num-1)*num/2) / num
    start = (total - (num - 1) * num // 2) // num
    return [start + i for i in range(num)]