# https://programmers.co.kr/learn/courses/30/lessons/67259
# title: 경주로 건설
# start: 2022-03-19 02:37:04 AM
# end:   2022-03-19 04:57:04 AM

from collections import deque

# 0: empty, 1: wall


def solution(board):
    N = len(board)
    cost = [[[1e9] * N for _ in range(N)] for _ in range(4)]
    bfs_q = deque([])

    # 상 하 좌 우
    # 0  1  2  3
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for dir in range(4):
        cost[dir][0][0] = 0

    # 오른쪽
    if board[0][1] == 0:
        cost[3][0][1] = 100
        bfs_q.append((3, 0, 1))

    # 아래쪽
    if board[1][0] == 0:
        cost[1][1][0] = 100
        bfs_q.append((1, 1, 0))

    while(bfs_q):
        prev_dir, i, j = bfs_q.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 1:
                    continue

                dir_cost = 100 if prev_dir == dir else 600
                new_cost = cost[prev_dir][i][j] + dir_cost

                if new_cost < cost[dir][ni][nj]:
                    cost[dir][ni][nj] = new_cost
                    bfs_q.append((dir, ni, nj))

    min_cost = min([cost[dir][-1][-1] for dir in range(4)])
    return min_cost
