# https://www.acmicpc.net/problem/9461
# title: 파도반 수열
# start: 2022-03-20 06:54:49 PM
# end:   2022-03-20 7:01:49 PM

def solution(N):
    dp = [1, 1, 1] + [0] * (abs(N-3))

    for i in range(3, N):
        dp[i] = dp[i-3] + dp[i-2]

    return dp[N-1]


if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        number = int(input())
        result.append(number)
    result = [solution(x) for x in result]
    print(*result, sep='\n')
