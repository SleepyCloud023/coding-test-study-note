# https://www.acmicpc.net/problem/1697
# title: 숨바꼭질
# start: 2022-03-19 12:54:51 AM
# end:   2022-03-19 01:11:00 AM


from collections import deque


def get_next_node(node: int, mode: int):
    if mode == 0:
        return node - 1
    elif mode == 1:
        return node + 1
    else:
        return node * 2


def bfs(src, dst):
    dist = [0] * 400001
    dist[src] = 1

    bfs_q = deque([src])
    while(bfs_q):
        cur_node = bfs_q.popleft()

        for mode in range(3):
            next_node = get_next_node(cur_node, mode)

            if not 0 <= next_node <= 400000:
                continue

            if dist[next_node] == 0:
                dist[next_node] = dist[cur_node] + 1
                bfs_q.append(next_node)

            if next_node == dst:
                return dist[next_node]


if __name__ == '__main__':
    src, dst = map(int, input().split())
    result = bfs(src, dst)
    print(result - 1)
