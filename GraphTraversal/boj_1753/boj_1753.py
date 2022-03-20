# https://www.acmicpc.net/problem/1753
# title: 최단경로
# start: 2022-03-20 11:36:51 PM
# end:   2022-03-20 12:15:51 PM

import heapq
import math
import sys
input = sys.stdin.readline


def bfs(V, graph, start):
    # 0 1 .... V
    # 0번 v는 무시
    dist = [1e9] * (V+1)
    dist[0] = 0
    dist[start] = 0
    Q = [(0, start)]

    while(Q):
        node_dist, now = heapq.heappop(Q)

        # 노드가 Q에 삽입되는 시점 이후에 해당 노드의 거리가 갱신되어 다시 삽입됨
        if dist[now] < node_dist:
            continue

        for next_node, cost in graph[now]:
            if node_dist + cost < dist[next_node]:
                dist[next_node] = node_dist + cost
                heapq.heappush(Q, (dist[next_node], next_node))

    return dist[1:]


if __name__ == '__main__':
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    start = int(input())

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    result = bfs(V, graph, start)

    for dist in result:
        if dist == 1e9:
            print('INF')
        else:
            print(dist)
