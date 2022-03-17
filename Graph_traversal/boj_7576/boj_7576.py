# https://www.acmicpc.net/problem/7576
# title: 토마토
# start: 2022-03-18 02:45:48 AM
# end:   2022-03-18 03:32:48 AM

from collections import deque
import sys
input = sys.stdin.readline


# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 빈 칸
def bfs(M, N, matrix, start):
    count = 0
    changed_tomato = []

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    i, j = start

    for dir in range(4):
        #print(i, dir)
        ni = i + di[dir]
        nj = j + dj[dir]

        if ni < 0 or nj < 0 or ni >= M or nj >= N:
            continue

        # 전파 방향의 토마토가 익지 않은 토마토인 경우
        if matrix[ni][nj] == 0:
            matrix[ni][nj] = 1
            count += 1
            changed_tomato.append((ni, nj))

    return count, changed_tomato


def count_day(M, N, matrix, good_tomato: list):
    num_day = 0

    while(True):
        count = 0
        next_tomato = []

        # 어제 익은 토마토를 순회하며 전파
        for (i, j) in good_tomato:
            count_changed, tomato_changed = bfs(M, N, matrix, (i, j))
            count += count_changed
            next_tomato += tomato_changed

        if count == 0:
            break

        num_day += 1
        good_tomato = next_tomato

    has_yet_tomato = False

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                has_yet_tomato = True
                break

    return -1 if has_yet_tomato else num_day


if __name__ == '__main__':
    width, height = map(int, input().split())
    matrix = []
    good_tomato = []

    for i in range(height):
        row = list(map(int, input().split()))
        for j in range(width):
            if row[j] == 1:
                good_tomato.append((i, j))
        matrix.append(row)

    result = count_day(height, width, matrix, good_tomato)
    print(result)
