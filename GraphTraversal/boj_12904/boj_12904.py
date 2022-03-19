# https://www.acmicpc.net/problem/1260
# DFS와 BFS
# 6:43 start

from collections import deque
import sys
read = sys.stdin.readline


def dfs(graph: list, visited: list, start: int):
    stack = deque([start])

    while(stack):
        top = stack.pop()

        if not visited[top]:
            print(top, end=' ')
            visited[top] = True

            for node in graph[top][::-1]:
                if visited[node] == False:
                    stack.append(node)
    print()


def bfs(graph: list, visited: list, start: int):
    q = deque([start])
    visited[start] = True

    while(q):
        top = q.popleft()
        print(top, end=' ')

        for node in graph[top]:
            if visited[node] == False:
                q.append(node)
                visited[node] = True
    print()


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)

    graph = [sorted(graph[i]) for i in range(N+1)]
    visited = [False] * (N+1)

    dfs(graph, visited[:], V)
    bfs(graph, visited[:], V)
