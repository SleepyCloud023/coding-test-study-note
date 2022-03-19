# https://www.acmicpc.net/problem/12851
# title: 숨바꼭질2
# start: 2022-03-19 01:20:15 AM
# end:   2022-03-19 02:11:00 AM
# 질문게시판에서 힌트 얻음

from collections import deque


def get_next_node(node, dir):
    if dir == 0:
        return node + 1
    elif dir == 1:
        return node - 1
    else:
        return 2 * node


def bfs(src: int, dst: int):
    count = 0
    dist = [0] * 400000
    dist[src] = 1

    bfs_q = deque([src])
    while(bfs_q):
        cur_node = bfs_q.popleft()

        for dir in range(3):
            next_node = get_next_node(cur_node, dir)

            if not 0 <= next_node < 400000:
                continue

            target = dist[dst]
            if target != 0 and dist[cur_node] >= target:
                continue

            if next_node == dst:
                count += 1

            next_distance = dist[cur_node] + 1
            if dist[next_node] == 0 or dist[next_node] == next_distance:
                dist[next_node] = next_distance
                bfs_q.append(next_node)

    return dist[dst] - 1, max(count, 1)


if __name__ == '__main__':
    src, dst = map(int, input().split())
    result = bfs(src, dst)
    print(*result, sep='\n')
