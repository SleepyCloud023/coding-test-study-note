# https://www.acmicpc.net/problem/1463
# title: 1로 만들기
# start: 2022-03-20 09:30:12 PM
# end:   2022-03-20 09:45:12 PM

def update_dp(N, dp, index, value):
    if index <= N:
        dp[index] = min(dp[index], value)


def solution(N):
    # N+1 배열: 0...N
    dp = [0, 0] + [1e9] * abs(N-1)

    for i in range(1, N):
        plus_1 = i + 1
        double = 2 * i
        triple = 3 * i

        update_dp(N, dp, plus_1, dp[i] + 1)
        update_dp(N, dp, double, dp[i] + 1)
        update_dp(N, dp, triple, dp[i] + 1)

    return dp[N]


if __name__ == '__main__':
    N = int(input())
    result = solution(N)
    print(result)
