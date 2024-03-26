def solution(N, stages):
    stage_counts = [0] * (N + 2)
    for stage in stages:
        stage_counts[stage] += 1
    
    failure_rate = {}
    filtered_stages = stages
    for i in range(1, N+1):
        filtered_stages = list(filter(lambda x: x >= i, filtered_stages))
        if len(filtered_stages) == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = (stage_counts[i] / len(filtered_stages))
    sorted_failure_rate = [k for k, v in sorted(failure_rate.items(), key=lambda x: (-x[1], int(x[0])))]
    return sorted_failure_rate
