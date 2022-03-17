# https://www.acmicpc.net/problem/1012
# 유기농 배추
# start: 2022-03-18 02:30:21 AM
# end:   2022-03-18 02:42:21 AM

from collections import deque


def bfs(M: int, N: int, matrix: list, start: tuple):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = deque([start])
    while(q):
        i, j = q.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if ni < 0 or nj < 0 or ni >= M or nj >= N:
                continue

            if matrix[ni][nj] == 1:
                matrix[ni][nj] = 0
                q.append((ni, nj))


def solution(M: int, N: int, matrix: list):
    count = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                continue

            bfs(M, N, matrix, (i, j))
            count += 1

    return count


if __name__ == '__main__':
    num_test = int(input())
    for _ in range(num_test):
        M, N, num_edge = map(int, input().split())
        matrix = [[0] * N for _ in range(M)]
        for _ in range(num_edge):
            m, n = map(int, input().split())
            matrix[m][n] = 1

        print(solution(M, N, matrix))
