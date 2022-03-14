# https://www.acmicpc.net/problem/2212
# 센서

# 3:58 start
# 4:18 end => 20분


def solution(num_wifi: int, sensor_list: list):
    sensor_list.sort()

    num_sensor = len(sensor_list)
    if num_sensor == 1:
        return 0

    diff_list = []

    for i in range(1, num_sensor):
        diff = sensor_list[i] - sensor_list[i-1]
        diff_list.append(diff)
    diff_list.sort()

    result = sensor_list[-1] - sensor_list[0]
    if num_wifi > 1:
        cut_count = num_wifi - 1
        result -= sum(diff_list[-cut_count:])

    return result


if __name__ == '__main__':
    N = int(input())
    num_wifi = int(input())
    sensor_list = list(map(int, input().split()))
    result = solution(num_wifi, sensor_list)
    print(result)
