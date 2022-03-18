# https://www.acmicpc.net/problem/2798
# title: 블랙잭
# start: 2022-03-18 10:39:55 PM
# end:   2022-03-18 10:48:30 PM

from itertools import combinations


def get_sum_combi_3(number_list):
    combi_3 = combinations(number_list, 3)
    combi_3 = [sum(x) for x in combi_3]
    return combi_3


def get_max_number(number_list, M):
    max_number = 0

    for number in number_list:
        if number > M:
            continue
        max_number = max(max_number, number)

    return max_number


if __name__ == '__main__':
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    sum_number = get_sum_combi_3(number_list)
    result = get_max_number(sum_number, M)
    print(result)
