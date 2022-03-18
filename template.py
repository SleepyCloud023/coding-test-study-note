import requests
import argparse
import os
import time
import re


def get_number_from_url(url: str) -> str:
    match_object = re.match(r'.*/(\d+)$', url)
    if match_object:
        number = match_object.group(1)
        return number
    else:
        raise ValueError('can not find postfix number')


def boj_make_dir(dir_path: str):
    try:
        os.mkdir(dir_path)
    except:
        print('target directory already exists')
        print('update internal sourcefile')


def boj_make_file(file_path: str, url: str, cur_time_stamp: str):
    with open(file_path, 'w') as fp:
        fp.write(f'# {url}\n')
        fp.write(f'# title: \n')
        fp.write(f'# start: {cur_time_stamp}\n')
        fp.write(f'# end:   {cur_time_stamp}\n')


def boj_make_template(url: str, category='./Greedy'):
    cur_time = time.localtime()
    cur_time_stamp = time.strftime('%Y-%m-%d %I:%M:%S %p', cur_time)

    problem_number = get_number_from_url(url)
    dir_path = f'{category}/boj_{problem_number}'
    file_path = f'{dir_path}/boj_{problem_number}.py'

    boj_make_dir(dir_path)
    boj_make_file(file_path, url, cur_time_stamp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make template for BOJ problem solving')
    parser.add_argument('url', type=str, help='url of problem')
    parser.add_argument('--title', '-t', type=str, help='title of problem')
    args = parser.parse_args()

    if (args.title):
        print(args.title)
