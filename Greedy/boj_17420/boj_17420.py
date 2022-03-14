# https://www.acmicpc.net/problem/17420
# 깊콘이 넘쳐흘러


import heapq
import sys
input = sys.stdin.readline


def solution(N, left_days: list, d_days: list):
    count = 0
    min_heap = []
    ticket_of_day = dict()

    for i in range(N):
        left_day = left_days[i]
        d_day = d_days[i]
        heapq.heappush(min_heap, (left_day, d_day))
        ticket_of_day[d_day] = ticket_of_day.get(d_day, 0) + 1

    for d_day in sorted(ticket_of_day.keys()):
        num_d_day = ticket_of_day[d_day]
        while(num_d_day > 0):
            left, d = heapq.heappop(min_heap)
            if d != d_day:
                add_count = max(d - left, 0) // 30 + 1
                count += add_count
                left += 30 * add_count
                heapq.heappush(min_heap, (left, d))
            elif d == d_day:
                if left < d:
                    count += 1
                    left += 30
                    heapq.heappush(min_heap, (left, d_day))
                else:
                    num_d_day -= 1

    return count


if __name__ == '__main__':
    N = int(input())
    left_days = list(map(int, input().split()))
    d_days = list(map(int, input().split()))
    result = solution(N, left_days, d_days)
    print(result)
