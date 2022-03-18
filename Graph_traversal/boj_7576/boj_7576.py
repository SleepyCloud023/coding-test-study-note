# https://www.acmicpc.net/problem/7576
# title: 토마토
# start: 2022-03-18 02:45:48 AM
# end:   2022-03-18 03:32:48 AM

from collections import deque
import sys
input = sys.stdin.readline


# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 빈 칸
def bfs(M: int, N: int, matrix: list, good_tomato: list):
    bfs_q = deque(good_tomato)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while(bfs_q):
        i, j = bfs_q.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if ni < 0 or nj < 0 or ni >= M or nj >= N:
                continue

            # 전파 방향의 토마토가 익지 않은 토마토인 경우
            if matrix[ni][nj] == 0:
                matrix[ni][nj] = matrix[i][j] + 1
                bfs_q.append((ni, nj))


def count_day(M, N, matrix, good_tomato: list):
    max_tomato = 0
    has_yet_tomato = False

    bfs(M, N, matrix, good_tomato)

    for row in matrix:
        for cur_tomato in row:
            if cur_tomato == 0:
                has_yet_tomato = True
            else:
                max_tomato = max(max_tomato, cur_tomato)

    return -1 if has_yet_tomato else (max_tomato - 1)


if __name__ == '__main__':
    width, height = map(int, input().split())
    matrix = []
    good_tomato = []

    for i in range(height):
        row = list(map(int, input().split()))
        matrix.append(row)

        for j in range(width):
            if row[j] == 1:
                good_tomato.append((i, j))

    result = count_day(height, width, matrix, good_tomato)
    print(result)
