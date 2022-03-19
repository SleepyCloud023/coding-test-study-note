# BinarySearch/8_3
# title: 개미전사
# start: 2022-03-19 11:28:14 PM
# end:   2022-03-19 11:28:14 PM

import sys
input = sys.stdin.readline

dp = []


def count(value_list: list, start: int, end: int):
    if start > end:
        return 0

    if dp[start] != 0:
        return dp[start]

    if start == end:
        dp[start] = value_list[start]
        return dp[start]

    v1 = value_list[start] + count(value_list, start + 2, end)
    v2 = count(value_list, start + 1, end)

    result = max(v1, v2)
    dp[start] = result

    return dp[start]


if __name__ == '__main__':
    N = int(input())
    value_list = list(map(int, input().split()))
    dp = [0] * N
    result = count(value_list, 0, N-1)
    print(result)
