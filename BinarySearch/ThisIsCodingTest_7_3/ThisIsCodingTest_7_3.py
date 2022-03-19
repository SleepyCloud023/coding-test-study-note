# BinarySearch/7_3
# title: 떡볶이 떡 만들기
# start: 2022-03-19 10:42:57 PM
# end:   2022-03-19 10:57:57 PM

import sys
input = sys.stdin.readline


def get_min_H(goal: int, choco_list):
    result = 0
    start = 0
    end = max(choco_list)

    while (start <= end):
        sum_choco = 0
        mid = (start + end) // 2

        for choco in choco_list:
            if choco > mid:
                sum_choco += choco - mid

        if sum_choco >= goal:
            result = mid
            start = mid + 1

        else:
            end = mid - 1

    return result


if __name__ == '__main__':
    num_choco, goal = map(int, input().split())
    choco_list = list(map(int, input().split()))
    result = get_min_H(goal, choco_list)
    print(result)
