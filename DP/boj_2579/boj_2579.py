# https://www.acmicpc.net/problem/2579
# title: 계단 오르기
# start: 2022-03-20 07:22:13 PM
# end:   2022-03-20 07:58:13 PM


def solution(N, point):
    # 2 x N+1
    dp = [[0] * (N+1) for _ in range(2)]
    dp[0][1] = point[1]
    dp[1][1] = point[1]

    for cur in range(N):
        next = cur+1

        dp[1][next] = max(dp[1][next], dp[0][cur] + point[next])

        next_2 = cur+2
        if next_2 <= N:
            dp[0][next_2] = max(dp[0][next_2], dp[0][cur] +
                                point[next_2], dp[1][cur] + point[next_2])

    return max(dp[0][N], dp[1][N])


if __name__ == '__main__':
    N = int(input())
    point = [0]
    for _ in range(N):
        point.append(int(input()))
    result = solution(N, point)
    print(result)
