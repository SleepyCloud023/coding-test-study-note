# https://www.acmicpc.net/problem/1912
# title: 연속합
# start: 2022-03-21 10:38:44 AM
# end:   2022-03-21 10:50:44 AM


def solution(N: int, arr: list):
    # i번째 숫자를 선택했을 때 연속된 수열 중 가장 큰 수열의 합
    dp = [0] * (N+1)

    for i in range(1, N+1):
        cur_number = arr[i-1]
        dp[i] = max(cur_number, cur_number + dp[i-1])

    return max(dp[1:])


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    result = solution(N, arr)
    print(result)
