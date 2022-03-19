# https://www.acmicpc.net/problem/16940
# title: BFS 스페셜 저지
# start: 2022-03-18 04:03:20 AM
# end:   2022-03-18 15:24:00 AM

from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph: list, order: list):
    first_node = order[0]
    first_set = {first_node}

    if first_node != 1:
        return 0

    bfs_q = deque([first_set])
    visited = {first_node}

    idx_order = 0
    while(bfs_q):
        cur_node_set = bfs_q.popleft()
        cur_order_list = order[idx_order: idx_order + len(cur_node_set)]
        idx_order += len(cur_node_set)

        #print(f'cur_set: {cur_node_set} cur_order_list: {cur_order_list}')
        for node in cur_order_list:
            if node not in cur_node_set:
                return 0

            elif node in cur_node_set:
                next_node_set = set(graph[node]) - visited
                if next_node_set:
                    visited.update(next_node_set)
                    bfs_q.append(next_node_set)

    return 1


if __name__ == '__main__':
    N = int(input())
    num_edge = N-1

    graph = [[] for _ in range(N+1)]

    for _ in range(num_edge):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)

    order = list(map(int, input().split()))

    result = bfs(graph, order)
    print(result)
