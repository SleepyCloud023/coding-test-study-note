# https://www.acmicpc.net/problem/2258
# 정육점

import sys
input = sys.stdin.readline

# 5:05 start
# 고기: (무게, 가격)


def solution(goal_meat: int, meat_list: list) -> int:
    meat_list.sort(key=lambda x: (x[1], -x[0]))

    best_price = 1e11
    best_price_sub = 1e11

    cur_weight = 0
    prev_price = -1
    for (weight, price) in meat_list:
        cur_weight += weight

        if prev_price != price:
            sub_price = price
            prev_price = price

            if cur_weight >= goal_meat:
                best_price = price
                break

        elif prev_price == price:
            if cur_weight < goal_meat:
                sub_price += price

            if cur_weight >= goal_meat:
                best_price_sub = sub_price + price

    best_price = min(best_price, best_price_sub)
    if best_price >= 1e10:
        best_price = -1
    return best_price


if __name__ == '__main__':
    N, goal_meat = map(int, input().split())
    meat_list = []
    for _ in range(N):
        meat = tuple(map(int, input().split()))
        meat_list.append(meat)
    result = solution(goal_meat, meat_list)
    print(result)

# my_test_case = '''
# 7 14
# 2 4
# 4 5
# 4 5
# 4 5
# 4 5
# 4 5
# 10 100

# 15

# 3 10
# 2 4
# 4 5
# 4 5

# 10

# 4 3
# 1 2
# 3 2
# 2 2
# 5 7

# 2

# 10 10
# 2 3
# 2 4
# 2 5
# 3 1
# 1 3
# 7 9
# 7 3
# 8 4
# 10 3
# 3 10

# 3
# '''
