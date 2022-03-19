# https://www.acmicpc.net/problem/14461
# title: 소가 길을 건너간 이유 7
# start: 2022-03-20 04:45:36 AM
# end:   2022-03-20 05:36:36 AM

from collections import deque
import sys
input = sys.stdin.readline


def bfs(N: int, T: int, matrix: list):
    dist = [[0] * N for _ in range(N)]

    Q = deque([(0, 0)])
    dist[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dir = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
    point = (3, 0)

    for mode in range(4):
        di, dj = dir[mode]
        for _ in range(3):
            point = (point[0] + di, point[1] + dj)
            dx.append(point[0])
            dy.append(point[1])
    # print(dx)
    # print(dy)

    while(Q):
        x, y = Q.popleft()

        for dir in range(len(dx)):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx >= N-1 and ny >= N-1:
                count_move = abs((N-1) - x) + abs((N-1) - y)
                new_cost = dist[x][y] + count_move * T

                if count_move == 3:
                    new_cost += matrix[-1][-1]
                dist[-1][-1] = min(dist[-1][-1], new_cost)

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = dist[x][y] + 3 * T + matrix[nx][ny]

                if dist[nx][ny] == 0 or new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    Q.append((nx, ny))

    return dist[-1][-1]


if __name__ == '__main__':
    N, T = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    result = bfs(N, T, matrix)
    print(result)
