# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42883

from collections import deque


def solution(number, k):
    answer = ''
    result_list = []
    upper_deq = deque([])
    lower_deq = deque(number)
    while(k > 0 and lower_deq):
        if (not upper_deq):
            upper_deq.append(lower_deq.popleft())
        left_number = upper_deq[-1]
        right_number = lower_deq[0]
        if (left_number >= right_number):
            upper_deq.append(lower_deq.popleft())
        elif (left_number < right_number):
            k -= 1
            del upper_deq[-1]

    result_list = list(upper_deq + lower_deq)
    if (k > 0):
        result_list = result_list[:-k]
    answer = ''.join(result_list)
    return answer
