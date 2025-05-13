def solution(lines):
    # 각 좌표가 몇 개의 선분에 포함되는지 카운트하기 위한 딕셔너리
    line_count = {}
    
    # 모든 선분의 범위에 해당하는 좌표에 카운트 증가
    for start, end in lines:
        for i in range(start, end):  # end-1까지만 포함 (길이 계산은 구간으로)
            if i not in line_count:
                line_count[i] = 0
            line_count[i] += 1
    
    # 두 개 이상의 선분이 겹치는 구간의 길이 계산
    overlap_length = 0
    for count in line_count.values():
        if count >= 2:
            overlap_length += 1
    
    return overlap_length