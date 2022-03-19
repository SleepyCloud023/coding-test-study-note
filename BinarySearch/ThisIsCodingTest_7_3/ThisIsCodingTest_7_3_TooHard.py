# BinarySearch/7_3
# title: 떡볶이 떡 만들기
# start: 2022-03-19 09:08:50 PM
# end:   2022-03-19 10:35:50 PM

# 구간합을 계산하는데 N log N(정렬) + N(순회) 시간 복잡도
# 현재 H의 구간합 배열에서의 인덱스 찾기 log N
# H 탐색은 이진 탐색이므로 0 ~ 10^10(10억) 구간에서 10^10 < 2^34 이므로 최악의 경우 34번 체크
# O(NlogN)

from bisect import bisect_right
import sys
input = sys.stdin.readline


def count_choco(sum_choco, H, idx_H):
    if idx_H == 0:
        return 0
    return sum_choco[idx_H-1] - idx_H * H


def find(goal: int, choco_list: list, sum_choco: list, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    mid_idx = len(choco_list) - bisect_right(choco_list, mid)

    choco_mid = count_choco(sum_choco, mid, mid_idx)

    if choco_mid >= goal:
        return mid
    else:
        return find(goal, choco_list, sum_choco, start, mid - 1)


def get_max_H(goal: int, num_choco: int, choco_list: list):
    choco_list.sort()
    sum_choco = [0] * (num_choco)
    sum_choco[0] = choco_list[-1]

    # sum_choco[k] => 뒤에서 k번째까지의 초코의 누적합
    for i in range(1, num_choco):
        sum_choco[i] = sum_choco[i-1] + choco_list[-i-1]

    best_choco_H = 0
    start = 0
    end = choco_list[-1]
    while(True):
        next_choco_H = find(goal, choco_list, sum_choco, start, end)
        if next_choco_H == -1:
            break
        else:
            best_choco_H = next_choco_H
            start = best_choco_H + 1

    return best_choco_H


if __name__ == '__main__':
    num_choco, goal = map(int, input().split())
    choco_list = list(map(int, input().split()))
    max_H = get_max_H(goal, num_choco, choco_list)
    print(max_H)
