import sys
from collections import deque

input = sys.stdin.readline


def solution(N: int, graph: list, start: int):
    dist = [0] * N

    q = deque([start])
    dist[start] = 1

    while(q):
        cur_node = q.popleft()

        for next_node in graph[cur_node]:
            if dist[next_node] == 0:
                dist[next_node] = dist[cur_node] + 1
                q.append(next_node)

    count = 0
    for path_length in dist:
        if path_length > 2:
            count += 1

    return count


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)

    count = [solution(N, graph, node) for node in range(N)]
    result = sum(count)
    print(result)


my_test = '''
5 4
0 1
0 2
1 3
1 4
'''
