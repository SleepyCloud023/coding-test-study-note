# https://www.acmicpc.net/problem/1543
# 등수매기기

import sys
input = sys.stdin.readline


def solution(N: int, rank_list: list):
    result = 0
    rank_list.sort()
    for idx, rank in enumerate(rank_list):
        result += abs(rank - (idx+1))
    return result


if __name__ == '__main__':
    N = int(input())
    rank_list = []
    for _ in range(N):
        rank_list.append(int(input()))
    result = solution(N, rank_list)
    print(result)
