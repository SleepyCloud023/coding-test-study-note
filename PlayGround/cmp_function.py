# url: https://www.acmicpc.net/problem/7568
# title: 덩치

# 덩치 문제로 cmp_to_key 함수 연습
# bisect 모듈의 경우 key parameter API의 이해가 필요할 듯 함
# TODO: aplly cmp_to_key to key param of bisect module
# NOTE: 그냥 클래스로 각 원소를 정렬하고 magic method 사용하는게 좋을듯

from functools import cmp_to_key
import bisect


def node_compare(left, right):
    '''
    return 
    if left > right:  1
    if left == right: 0
    if left < right: -1
    '''
    if left[0] > right[0] and left[1] > right[1]:
        return -1
    elif left[0] < right[0] and left[1] < right[1]:
        return 1
    else:
        return 0


def solution(N, arr):
    arr.sort(key=cmp_to_key(node_compare))
    rank = []
    cur_idx = 0

    while(cur_idx < N):
        cur_value = arr[cur_idx]
        #idx_first_next_rank = bisect.bisect_right(arr, cur_value, lo=cur_idx)
        idx_first_next_rank = bisect.bisect_right(
            arr, cur_value, key=cmp_to_key(node_compare))
        print(
            f'cur_idx: {cur_idx}, cur_value:{cur_value} ,next_idx: {idx_first_next_rank}')
        rank += [len(rank) + 1] * (idx_first_next_rank - cur_idx)
        cur_idx = idx_first_next_rank
    print(arr)
    print(rank)
    return rank


if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    result = solution(N, arr)
    print(result)
