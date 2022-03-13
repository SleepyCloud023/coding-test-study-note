# https://www.acmicpc.net/problem/11501
# 주식

import sys
input = sys.stdin.readline


def solution(days: int, price_list: list):
    result = 0
    buy_list = []
    has_hope = [True] * days
    max_value = 0
    for day in range(1, days+1):
        if max_value <= price_list[-day]:
            has_hope[-day] = False
            max_value = price_list[-day]

    for day in range(days - 1):
        today, next_day = price_list[day: day+2]

        if has_hope[day]:
            buy_list.append(today)
        else:
            if buy_list:
                result += today * len(buy_list) - sum(buy_list)
                buy_list = []

        if(buy_list):
            result += next_day * len(buy_list) - sum(buy_list)
    return result


if __name__ == '__main__':
    T = int(input())
    result = []

    for _ in range(T):
        days = int(input())
        price_list = list(map(int, input().split()))
        result.append(solution(days, price_list))

    for profit in result:
        print(profit)
