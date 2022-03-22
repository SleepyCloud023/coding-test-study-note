# 11:34 시작
import bisect


def solution(info, query):
    answer = []
    people = []

    lang_dict = {'-': 0, 'cpp': 1, 'java': 2, 'python': 3}
    position_dict = {'-': 0, 'backend': 1, 'frontend': 2}
    level_dict = {'-': 0, 'junior': 1, 'senior': 2}
    food_dict = {'-': 0, 'chicken': 1, 'pizza': 2}

    for idx, info_string in enumerate(info):
        lang, position, level, food, score = info_string.split()
        score = int(score)
        person = (score, lang_dict[lang], position_dict[position],
                  level_dict[level], food_dict[food])
        people.append(person)

    people.sort(key=lambda x: x[0])
    # print(people)

    for q in query:
        #       1     2         3      4
        lang, position, level, food_score = q.split(' and ')
        food, score = food_score.split()
        score = int(score)

        lang = lang_dict[lang]
        position = position_dict[position]
        level = level_dict[level]
        food = food_dict[food]

        idx_first = bisect.bisect_left(people, (score, 0, 0, 0, 0))

        count = 0

        for person in people[idx_first:]:
            if lang != 0:
                if person[1] != lang:
                    continue
            if position != 0:
                if person[2] != position:
                    continue
            if level != 0:
                if person[3] != level:
                    continue
            if food != 0:
                if person[4] != food:
                    continue
            count += 1

        answer.append(count)
    return answer
