# url: https://www.acmicpc.net/problem/7568
# title: 덩치

# 덩치 문제로 cmp_to_key 함수 연습
# NOTE: 클래스로 정렬 기준 정의(:magic method)

from functools import cmp_to_key, total_ordering
import bisect


@total_ordering
class Person:
    def __init__(self, number, weight, height):
        self.number = number
        self.weight = weight
        self.height = height

    def __lt__(self, other):
        return self.height > other.height and self.weight > other.weight

    def __gt__(self, other):
        return self.height < other.height and self.weight < other.weight

    def __repr__(self):
        return f'(n: {self.number} w: {self.weight} v:{self.height})'


def solution(N: int, arr: list):
    arr.sort()
    rank = []
    cur_idx = 0

    while(cur_idx < N):
        cur_value = arr[cur_idx]
        idx_first_next_rank = bisect.bisect_right(arr, cur_value)
        # print(
        #    f'cur_idx: {cur_idx}, cur_value:{cur_value} ,next_idx: {idx_first_next_rank}')
        rank += [len(rank) + 1] * (idx_first_next_rank - cur_idx)
        cur_idx = idx_first_next_rank

    # print(arr)
    result = [0] * N
    for idx, person in enumerate(arr):
        # print(person)
        result[person.number] = rank[idx]

    return result


if __name__ == '__main__':
    N = int(input())
    arr = []
    for number in range(N):
        weight, height = map(int, input().split())
        arr.append(Person(number, weight, height))
    result = solution(N, arr)
    print(*result)
