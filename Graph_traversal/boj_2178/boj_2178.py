# https://www.acmicpc.net/problem/2178
# 미로 탐색
# 8:20 start
# 9:25 end => 1시간 5분

from collections import deque
import sys
input = sys.stdin.readline


def solution(graph: list, N: int, M: int):
    count_map = [[0] * M for _ in range(N)]

    start = (0, 0)
    # R L D U
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([start])
    count_map[0][0] = 1

    while(q):
        (y, x) = q.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if graph[ny][nx] == 0:
                continue

            if count_map[ny][nx] == 0:
                count_map[ny][nx] = count_map[y][x] + 1
                q.append((ny, nx))

    return count_map[N-1][M-1]


if __name__ == '__main__':
    graph = []
    N, M = map(int, input().split())
    for _ in range(N):
        row = list(map(int, input().rstrip()))
        graph.append(row)
    result = solution(graph, N, M)
    print(result)
