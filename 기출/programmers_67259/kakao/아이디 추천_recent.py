# 10:46 ~ 11:09

def solution(new_id):
    answer = ''
#     1
    new_id = new_id.lower()
    result = []
#     2
    for char in new_id:
        if char.isalpha() or char.isdigit():
            result.append(char)
        elif char in ['.', '-', '_']:
            result.append(char)
        else:
            continue
    result = ''.join(result)
    # 3
    while(result.find('..') != -1):
        result = result.replace('..', '.')

    # 4
    result = list(result)
    while(result and result[0] == '.'):
        result.pop(0)
    while(result and result[-1] == '.'):
        result.pop()
# #     5
    if not result:
        result = ['a']
# #     6
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result.pop()
# #     7
    if len(result) <= 2:
        result = result + [result[-1]]*3
        result = result[:3]

    new_id = ''.join(result)
    print(new_id)
    return new_id
