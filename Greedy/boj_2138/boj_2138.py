# https://www.acmicpc.net/problem/2138
# 전구와 스위치
# 2:34 start
# 3:45 end

# 질문 게시판에서 구현 힌트 얻음

# 1) 버튼을 두 번 누른다면 누르지 않은 것과 같다
# 2) 버튼을 누른 횟수만 같다면 순서는 상관이 없다
# 1번 스위치를 누를지 말지 결정해준다면
# 이후 순서대로 스위치를 누르는 경우의 수는 1개이고
# 1번 스위치의 분기에 따른 경우의 수를 비교해 주면 된다.


def solution(N: int, diff_list: list) -> int:
    count_on = 1
    on_list = [1-diff_list[0], 1-diff_list[1]] + diff_list[2:]
    # 2번째 스위치부터 마지막 스위치 전까지
    for i in range(1, N-1):
        prev_state = on_list[i-1]
        if prev_state != 0:
            on_list[i-1] = 1 - on_list[i-1]
            on_list[i] = 1 - on_list[i]
            on_list[i+1] = 1 - on_list[i+1]
            count_on += 1
    prev_last, last = on_list[-2:]
    if (prev_last != last):
        count_on = 1e9
    else:
        count_on += last

    count_off = 0
    off_list = diff_list

    for i in range(1, N-1):
        prev_state = off_list[i-1]
        if prev_state != 0:
            off_list[i-1] = 1 - off_list[i-1]
            off_list[i] = 1 - off_list[i]
            off_list[i+1] = 1 - off_list[i+1]
            count_off += 1
    prev_last, last = off_list[-2:]
    if (prev_last != last):
        count_off = 1e9
    else:
        count_off += last

    result = min(count_on, count_off)
    return result if result != 1e9 else -1


if __name__ == '__main__':
    N = int(input())
    origin = input()
    output = input()
    diff_list = [0 if origin[i] == output[i] else 1 for i in range(N)]
    result = solution(N, diff_list)
    print(result)
