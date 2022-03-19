# https://www.acmicpc.net/problem/11047
# title: 동전 0
# start: 2022-03-20 01:04:47 AM
# end:   2022-03-20 01:11:00 AM

import sys
input = sys.stdin.readline


def count_coin(coin_list: list, K: int):
    coin_list.reverse()
    count = 0

    for coin in coin_list:
        Q, K = divmod(K, coin)

        if Q > 0:
            count += Q

        if K == 0:
            break

    return count


if __name__ == '__main__':
    N, K = map(int, input().split())
    coin_list = [int(input()) for _ in range(N)]
    result = count_coin(coin_list, K)
    print(result)
