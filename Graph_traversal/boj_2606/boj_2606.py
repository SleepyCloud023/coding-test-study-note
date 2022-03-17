# https://www.acmicpc.net/problem/2606
# start: 2022-03-18 01:56:05 AM
# end:   2022-03-18 02:03:05 AM

from collections import deque


def bfs(graph: list, visited):
    start = 1
    visited[start] = True
    q = deque([start])
    count = 0

    while(q):
        seed = q.popleft()

        for node in graph[seed]:
            if visited[node] == False:
                visited[node] = True
                q.append(node)
                count += 1

    return count


if __name__ == '__main__':
    num_node = int(input())
    num_edge = int(input())

    graph = [[] for _ in range(num_node+1)]
    visited = [False] * (num_node+1)
    for _ in range(num_edge):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)
    result = bfs(graph, visited)
    print(result)
