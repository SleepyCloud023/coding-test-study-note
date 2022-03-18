map_board = []
best_score = 10 ** 8

# dir : right 0, down 1, left 2, up 3


def find_path(score, pos, direction, is_visit, n):
    global map_board, best_score, history
    (x, y) = pos
    candidates = []
    right, down, left, up = (x+1, y), (x, y+1), (x-1, y), (x, y-1)
    dirs = [right, down, left, up]

    if pos == (n-1, n-1):
        if score < best_score:
            best_score = score
        return score

    if score >= best_score:
        return 10 ** 8

    for idx, next_pos in enumerate(dirs):
        (next_x, next_y) = next_pos
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
            if next_pos not in is_visit and map_board[next_y][next_x] == 0:
                if idx == direction or pos == (0, 0):
                    candidates.append(
                        find_path(100 + score, next_pos, idx, is_visit | set([next_pos]), n))
                else:
                    candidates.append(
                        find_path(600 + score, next_pos, idx, is_visit | set([next_pos]), n))

    if candidates == []:
        score = 10 ** 8
        return score
    else:
        result = min(candidates)
        return result


def solution(board):
    global map_board
    map_board = board
    best_score = 10 ** 8
    answer = 0
    pos = (0, 0)
    is_visit = set([pos])
    n = len(board)
    answer = find_path(0, pos, 0, is_visit, n)

    return answer
