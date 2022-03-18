# https://www.acmicpc.net/problem/7568
# title: 덩치
# start: 2022-03-18 11:10:35 PM
# end:   2022-03-18 11:34:35 PM


def get_rank(person_list: list):
    rank = [1] * len(person_list)
    num_person = len(person_list)

    for idx in range(num_person - 1):
        x, y = person_list[idx]
        for idx_other in range(idx + 1, num_person):
            x_o, y_o = person_list[idx_other]
            if x > x_o and y > y_o:
                rank[idx_other] += 1
            if x < x_o and y < y_o:
                rank[idx] += 1

    return rank


if __name__ == '__main__':
    N = int(input())
    person_list = []
    for _ in range(N):
        person = tuple(map(int, input().split()))
        person_list.append(person)
    result = get_rank(person_list)
    print(*result)
