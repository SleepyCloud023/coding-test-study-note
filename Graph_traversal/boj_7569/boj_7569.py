# https://www.acmicpc.net/problem/7569
# title: 토마토
# start: 2022-03-18 05:14:29 PM
# end:   2022-03-18 05:44:29 PM

from collections import deque
import sys
input = sys.stdin.readline


def bfs(M, N, H, matrix: list, good_tomato: list):
    bfs_q = deque(good_tomato)

    di = [-1, 1, 0, 0, 0, 0]
    dj = [0, 0, -1, 1, 0, 0]
    dk = [0, 0, 0, 0, -1, 1]

    while(bfs_q):
        k, i, j = bfs_q.popleft()

        for dir in range(6):
            nk = k + dk[dir]
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < M and 0 <= nk < H:
                if matrix[nk][ni][nj] == 0:
                    matrix[nk][ni][nj] = matrix[k][i][j] + 1
                    bfs_q.append((nk, ni, nj))


def check_tomato(M, N, H, matrix):
    day = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                cur_tomato = matrix[k][i][j]
                if cur_tomato == 0:
                    return -1
                else:
                    day = max(day, cur_tomato)
    return day - 1


def count_day(M: int, N: int, H: int, matrix: list, good_tomato: list):
    bfs(M, N, H, matrix, good_tomato)
    day = check_tomato(M, N, H, matrix)
    return day


if __name__ == '__main__':
    # M: 가로 N: 세로 H: 높이
    M, N, H = map(int, input().split())
    good_tomato = []
    matrix = []
    for k in range(H):
        plane = []
        for i in range(N):
            row = list(map(int, input().split()))
            plane.append(row)

            for j in range(M):
                if row[j] == 1:
                    good_tomato.append((k, i, j))
        matrix.append(plane)

    result = count_day(M, N, H, matrix, good_tomato)
    print(result)
