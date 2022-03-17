import requests
import argparse
import os
import time


def boj_make_dir(url: str, problem_number: int, category='./Greedy'):
    cur_time = time.localtime()
    cur_time_stamp = time.strftime('%Y-%m-%d %I:%M:%S %p', cur_time)

    dir_path = f'{category}/boj_{problem_number}'
    file_path = f'{dir_path}/boj_{problem_number}.py'

    os.mkdir(f'{category}/boj_{problem_number}')
    with open(file_path, 'w') as fp:
        fp.write(f'# {url}\n')
        fp.write(f'# title: \n')
        fp.write(f'# start: {cur_time_stamp}\n')
        fp.write(f'# end:   {cur_time_stamp}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make template for BOJ problem solving')
    parser.add_argument('url', type=str, help='url of problem')
    parser.add_argument('--title', '-t', type=str, help='title of problem')
    args = parser.parse_args()

    if (args.title):
        print(args.title)
