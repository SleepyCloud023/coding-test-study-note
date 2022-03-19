# https://www.acmicpc.net/problem/2293
# title: 동전 1
# start: 2022-03-20 01:19:30 AM
# end:   2022-03-20 04:09:00 AM

def solution(coin_list: list, K: int):
    dp = [0] * (K+1)
    dp[0] = 1

    for coin in coin_list:
        for number in range(coin, K + 1):
            dp[number] = dp[number] + dp[number - coin]

    return dp[K]


if __name__ == '__main__':
    num_coin, K = map(int, input().split())
    coin_list = []
    for _ in range(num_coin):
        coin = int(input())
        coin_list.append(coin)

    result = solution(coin_list, K)
    print(result)
