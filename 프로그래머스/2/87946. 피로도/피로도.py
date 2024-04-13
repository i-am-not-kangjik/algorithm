def dfs(current_k, dungeons, visited):
    max_explored = 0

    for i, (min_fatigue, consumption) in enumerate(dungeons):
        if not visited[i] and current_k >= min_fatigue:
            visited[i] = True
            next_k = current_k - consumption
            max_explored = max(max_explored, 1 + dfs(next_k, dungeons, visited))
            visited[i] = False

    return max_explored

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = dfs(k, dungeons, visited)
    return answer