import sys
input = sys.stdin.readline


def solution(N: int, graph: list, start: int):
    length_below_2 = 1 + len(graph[start])
    return N - length_below_2


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
