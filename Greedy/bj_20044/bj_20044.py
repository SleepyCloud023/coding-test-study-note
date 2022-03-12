# https://www.acmicpc.net/problem/20044
# Project Teams


def solution(N: int, w_list: list):
    w_list.sort()
    # 1 <= w <= 100,000
    min_sum = 200000
    for i in range(N):
        current_sum = w_list[i] + w_list[-(i+1)]
        min_sum = min(min_sum, current_sum)
    return min_sum


if __name__ == "__main__":
    N = int(input())
    w_list = list(map(int, input().split()))
    print(solution(N, w_list))
