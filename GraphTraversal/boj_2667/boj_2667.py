# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기
# start: 2022-03-18 02:07:21 AM
# end:   2022-03-18 02:22:00 AM

from collections import deque


def bfs(N: int, matrix: list, start: int):
    i, j = start

    if matrix[i][j] == 0:
        return 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = deque([start])
    matrix[i][j] = 0
    count = 1

    while(q):
        i, j = q.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue

            if matrix[ni][nj] == 1:
                count += 1
                matrix[ni][nj] = 0
                q.append((ni, nj))

    return count


if __name__ == '__main__':
    N = int(input())
    matrix = []
    for _ in range(N):
        row = list(map(int, input()))
        matrix.append(row)

    result = []
    for i in range(N):
        for j in range(N):
            count = bfs(N, matrix, (i, j))
            if count:
                result.append(count)

    result.sort()
    print(len(result))
    print(*result, sep='\n')
