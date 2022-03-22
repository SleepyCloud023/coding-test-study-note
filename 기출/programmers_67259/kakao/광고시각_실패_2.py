import heapq


def get_second(time):
    h, m, s = map(int, time.split(':'))
    return 3600 * h + 60 * m + s


def get_two_length(time):
    if len(time) == 1:
        return '0' + time
    else:
        return time


def get_hms(time):
    h, m = divmod(time, 3600)
    m, s = divmod(m, 60)
    return h, m, s


def solution(play_time, adv_time, logs):
    play_time = get_second(play_time)
    adv_time = get_second(adv_time)
    logs = [tuple(map(get_second, log.split('-'))) for log in logs]

    H = []
    check_point = [0, play_time - adv_time]
    logs.sort(key=lambda x: x[0])

    for i in range(len(logs)):
        start, end = logs[i]
        check_point.append(start)
        if end - adv_time >= 0:
            check_point.append(end - adv_time)

    check_point = sorted(list(set(check_point)))
    best = 0
    score = 0
    left_idx = 0
    prev_start = -1

#     H: (end, start)
    for cur_start in check_point:
        prev_start = cur_start
        # 광고 종료시간이 플레이 시간보다 길면 종료
        if cur_start + adv_time > play_time:
            break

        # 현재 시간보다 전에 끝난 로그 제거
        while (H and H[0][0] < cur_start):
            heapq.heappop(H)
        # 현재 시간 + 광고 길이보다 빠른 시작시간을 가지는 log 추가
        while (left_idx < len(logs)):
            next_start, next_end = logs[left_idx]
            if cur_start + adv_time > next_start:
                heapq.heappush(H, (next_end, next_start))
                left_idx += 1
            else:
                break

        cur_score = 0

        for log_end, log_start in H:
            duration_end = min(log_end, cur_start + adv_time)
            duration_start = max(cur_start, log_start)
            duration = duration_end - duration_start
            cur_score += duration

        if cur_score > score:
            score = cur_score
            best = cur_start

    h, m, s = map(str, get_hms(best))

    return f'{get_two_length(h)}:{get_two_length(m)}:{get_two_length(s)}'
