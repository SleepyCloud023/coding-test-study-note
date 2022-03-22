def convert_time_to_date(time):
    hour, time = divmod(time, 3600)
    minute, second = divmod(time, 60)
    result = [hour, minute, second]
    result = [str(x) if len(str(x)) == 2 else "0"+str(x) for x in result]
    result = ":".join(result)
    return result


def solution(play_time, adv_time, logs):
    answer = ''
    user_times = []
    candidates = []
    candidates_start_value = []

    play = play_time.split(":")
    adv = adv_time.split(":")
    play_time = int(play[0]) * 3600 + int(play[1]) * 60 + int(play[2])
    adv_time = int(adv[0]) * 3600 + int(adv[1]) * 60 + int(adv[2])

    for l in logs:
        start_log, end_log = l.split("-")
        start = start_log.split(":")
        end = end_log.split(":")
        start_time = int(start[0]) * 3600 + int(start[1]) * 60 + int(start[2])
        end_time = int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])
        user_times.append((start_time, end_time))
        candidates.append(start_time)
    user_times.sort(key=lambda x: x[1])
    candidates = sorted(list(set(candidates)))

    target_idx = 0
    max_idx = len(user_times)
    for start in candidates:
        value = 0
        idx = target_idx
        candi_start, candi_end = start, start + adv_time
        # 로그의 시작시각이 후보 구간의 종료시각보다 앞서는 경우
        while(idx < max_idx and user_times[idx][0] < candi_end):
            # 겹치는 러닝타임이 없으면 스킵
            if(user_times[idx][1] <= candi_start):
                target_idx += 1
                idx += 1
                continue
            # 겹치는 러닝타임이 존재 => (후보 시작시각, 후보 종료시각or 로그 종료시각)
            end = min(candi_end, user_times[idx][1])
            value += end - candi_start
            idx += 1

        candidates_start_value.append((candi_start, value))
        target_idx = 0

    candidates_start_value.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    answer = candidates_start_value[0][0]
    if answer + adv_time >= play_time:
        answer -= (answer + adv_time - play_time)
    answer = convert_time_to_date(answer)
    return answer
