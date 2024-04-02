def solution(X, Y):
    # 0부터 9까지 count하는 배열
    count_X = [0] * 10
    count_Y = [0] * 10
    for digit in X:
        count_X[int(digit)] += 1
    for digit in Y:
        count_Y[int(digit)] += 1
    
    # min을 사용해 같이 등장한 최소 count 찾기
    common_count = [min(count_X[d], count_Y[d]) for d in range(10)]
    
    # 짝꿍이 없거나 0인 경우 처리
    if sum(common_count) == 0:
        return "-1"
    elif sum(common_count[1:]) == 0:
        return "0"
    
    # 역순으로 같이 등장한 수 만큼 문자열 생성
    answer = ''.join(str(d) * common_count[d] for d in range(9, -1, -1))
    
    return answer