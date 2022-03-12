# 2021-10-11
# nqueen 문제 bfs 방식으로 해결하기

from collections import deque

# 현재 row(level) 와
# cols: 세로선, cross_ru: 우상향 대각선 (#elemnets=2n-1), cross_rd: 우하향 대각선 (#elemnets=2n-1)
# 정보를 담고있는 클래스

class nqueen_node:
    def __init__(self, row: int, cols: list, cross_ru: dict, cross_rd: dict):
        self.row = row
        self.cols = cols
        self.cross_ru = cross_ru
        self.cross_rd = cross_rd

# N 입력받기
n = int(input('input N: '))

# init

f_row = 0
f_cols = [-1] * n
f_cross_ru = dict()
f_cross_rd = dict()
first_node = nqueen_node(f_row, f_cols, f_cross_ru, f_cross_rd)

bfs_q = deque([first_node])
result = None
answer_count = 0

while(bfs_q):
    cur_node = bfs_q.popleft()
    row = cur_node.row
    cols = cur_node.cols
    cross_ru = cur_node.cross_ru
    cross_rd = cur_node.cross_rd
    
    if row == n:
        result = cur_node.cols
        break
        # answer_count += 1

    for next_col in range(n):
        # prunning
        # 세로선
        if cols[next_col] != -1: continue
        # 우상향 대각선
        if cross_ru.get(row+next_col, False) == True: continue
        # 우하향 대각선
        if cross_rd.get(row-next_col, False) == True: continue
        # prunning test passed
        next_row = row + 1
        next_cols = cols[:]
        next_cols[next_col] = row
        next_ru = cross_ru.copy()
        next_ru[row+next_col] = True
        next_rd = cross_rd.copy()
        next_rd[row-next_col] = True
        # queue에 추가
        next_node = nqueen_node(next_row, next_cols, next_ru, next_rd)
        bfs_q.append(next_node)

print(f'number of total cases: {answer_count}')
print(f'one case: {result}')
for col in result:
    row_star = ['-'] * n
    row_star[col] = '*'
    print(*row_star)


