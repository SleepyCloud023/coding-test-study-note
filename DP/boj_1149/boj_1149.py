# https://www.acmicpc.net/problem/1149
# title: RGB거리
# start: 2022-03-20 06:25:10 PM
# end:   2022-03-20 06:53:10 PM

import sys
input = sys.stdin.readline


def solution(N, rgb):
    # 3 x N dp 테이블
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = rgb[0]

    for i in range(1, N):
        dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[N-1])


if __name__ == '__main__':
    N = int(input())
    rgb_arr = []
    for _ in range(N):
        rgb = list(map(int, input().split()))
        rgb_arr.append(rgb)
    result = solution(N, rgb_arr)
    print(result)
