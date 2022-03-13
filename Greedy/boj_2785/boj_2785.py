# https://www.acmicpc.net/problem/2785
# 체인

# 6:51
# 7:35 => 44분
# 문제 이해하는데 시간이 너무 많이 걸렸음

from collections import deque
import sys
input = sys.stdin.readline


def solution(N: int, chain_list: deque):
    count = 0
    while(len(chain_list) > 1):
        short_chain = chain_list[0]
        last = chain_list.pop()
        pre_last = chain_list.pop()

        count += 1
        chain_list.append(pre_last + last)
        if short_chain == 1:
            chain_list.popleft()
        else:
            chain_list[0] -= 1
    return count


if __name__ == '__main__':
    N = int(input())
    chain_list = list(map(int, input().split()))
    chain_list.sort()
    result = solution(N, deque(chain_list))
    print(result)
