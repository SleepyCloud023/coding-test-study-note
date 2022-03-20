# https://www.acmicpc.net/problem/1932
# title: 정수 삼각형
# start: 2022-03-20 07:02:50 PM
# end:   2022-03-20 07:16:50 PM

import sys
input = sys.stdin.readline


def solution(N, arr):
    dp = []

    for length in range(1, N+1):
        dp.append([0] * length)

    dp[0][0] = arr[0][0]

    for row in range(N-1):
        for col, cur_dp in enumerate(dp[row]):
            dp[row + 1][col] = max(dp[row+1][col], cur_dp + arr[row+1][col])
            dp[row + 1][col + 1] = max(dp[row+1]
                                       [col + 1], cur_dp + arr[row+1][col+1])

    return max(dp[N-1])


if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    result = solution(N, arr)
    print(result)
