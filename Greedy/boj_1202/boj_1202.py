# https://www.acmicpc.net/problem/1202
# 보석도둑

from heapq import heappush, heappop
import sys

# stone_list 원소 = (M, V) => 무게, 가치
# bag_list 원소 = C => 무게


def solution(stone_list: list, bag_list: list) -> int:
    result = 0
    stone_list.sort(key=lambda x: x[0])
    bag_list.sort()
    heap = []
    len_stone_list = len(stone_list)
    stone_idx = 0

    for bag_weight in bag_list:
        while (stone_idx < len_stone_list):
            stone_weight, stone_value = stone_list[stone_idx]

            if stone_weight <= bag_weight:
                heappush(heap, -stone_value)
                stone_idx += 1
            else:
                break

        if (heap):
            result += -heappop(heap)

    return result


if __name__ == '__main__':
    N, K = map(int, input().split())
    stone_list = []
    bag_list = []
    for i in range(N):
        M, V = map(int, sys.stdin.readline().split())
        stone_list.append((M, V))
    for i in range(K):
        bag_weight = int(sys.stdin.readline())
        bag_list.append(bag_weight)

    print(solution(stone_list, bag_list))
