# https://www.acmicpc.net/problem/17420
# 깊콘이 넘쳐흘러


import heapq
import math
import sys
input = sys.stdin.readline


class Ticket:
    def __init__(self, d_day, left_day) -> None:
        self.d_day = d_day
        self.left_day = left_day

    def __lt__(self, other):
        if self.d_day < other.d_day:
            return True
        elif self.d_day == other.d_day:
            return self.left_day >= other.left_day
        else:
            return False


def solution(N, left_days: list, d_days: list):
    count = 0
    min_heap = []
    min_left = 0

    for i in range(N):
        left_day = left_days[i]
        d_day = d_days[i]
        heapq.heappush(min_heap, Ticket(d_day, left_day))

    while(min_heap):
        today = min_heap[0].d_day
        ticket_list = []

        while(min_heap and min_heap[0].d_day == today):
            ticket = heapq.heappop(min_heap)
            ticket_list.append(ticket)

        for ticket in ticket_list:
            bigger_day = max(ticket.d_day, min_left)

            if ticket.left_day < bigger_day:
                Q = math.ceil((bigger_day - ticket.left_day) / 30)
                ticket.left_day += Q * 30
                count += Q

        min_left = max([ticket.left_day for ticket in ticket_list])

    return count


if __name__ == '__main__':
    N = int(input())
    left_days = list(map(int, input().split()))
    d_days = list(map(int, input().split()))
    result = solution(N, left_days, d_days)
    print(result)

test_case = '''
4
24 2 3 29
25 30 30 30

=> 6
'''
