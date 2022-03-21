# https://www.acmicpc.net/problem/12015
# title: 가장 긴 증가하는 부분 수열 2
# start: 2022-03-21 10:21:38 AM
# end:   2022-03-21 10:31:38 AM

# NOTE: 나무위키 설명 참조

from bisect import bisect_left


def solution(N, arr):
    # 길이가 i인 증가하는 부분 수열들의 마지막 숫자 중 가장 작은 것
    dp = [0] + [1e9] * N

    max_length = 0

    for i in range(N):
        cur_number = arr[i]
        cur_idx = bisect_left(dp, cur_number)
        # 기존 길이가 cur_idx인 수열의 마지막 숫자보다 지금 숫자가 작으면 갱신
        dp[cur_idx] = min(dp[cur_idx], cur_number)

        max_length = max(max_length, cur_idx)

    return max_length


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    result = solution(N, arr)
    print(result)
