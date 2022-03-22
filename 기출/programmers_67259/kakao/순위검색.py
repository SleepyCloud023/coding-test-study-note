# 11:34 시작
# 제한 시간 내 실패

import bisect
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    people = []

    counter = defaultdict(list)

    for idx, info_string in enumerate(info):
        lang, position, level, food, score = info_string.split()
        score = int(score)
        condition_list = (lang, position, level, food)
        for num_wildcard in range(5):
            for C in combinations(range(4), num_wildcard):
                new_condition = list(condition_list)
                for idx in C:
                    new_condition[idx] = '-'
                counter[tuple(new_condition)].append(score)

    for condition in counter:
        counter[condition].sort()

    for q in query:
        #       1     2         3      4
        lang, position, level, food_score = q.split(' and ')
        food, score = food_score.split()
        score = int(score)

        people = counter[(lang, position, level, food)]
        idx_score = bisect.bisect_left(people, score)
        num_over_score = len(people) - idx_score

        answer.append(num_over_score)

    return answer
