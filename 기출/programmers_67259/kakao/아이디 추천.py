import re


def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    target = re.findall("[a-z0-9_.-]+", new_id)
    target = "".join(target)

    target = re.findall("([a-z0-9_-]+[.]?)[.]*", target)
    target = "".join(target)

    if target and target[-1] == ".":
        target = target[:-1]

    if target == "":
        target = "a"

    if len(target) > 15:
        target = target[:15]
        if target[-1] == ".":
            target = target[:-1]

    if len(target) <= 2:
        target += target[-1]
        target += target[-1]
        target = target[:3]
    answer = target
    return answer
