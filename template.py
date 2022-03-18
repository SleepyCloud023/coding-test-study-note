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


def make_dir(dir_path: str):
    try:
        os.mkdir(dir_path)
    except:
        print('target directory already exists')
        print('update internal sourcefile')


def make_file(file_path: str, url: str, cur_time_stamp: str):
    with open(file_path, 'w') as fp:
        fp.write(f'# {url}\n')
        fp.write(f'# title: \n')
        fp.write(f'# start: {cur_time_stamp}\n')
        fp.write(f'# end:   {cur_time_stamp}\n')


def make_template(prefix_site: str, url: str, category: str):
    cur_time = time.localtime()
    cur_time_stamp = time.strftime('%Y-%m-%d %I:%M:%S %p', cur_time)

    problem_number = get_number_from_url(url)
    dir_path = f'{category}/{prefix_site}_{problem_number}'
    file_path = f'{dir_path}/{prefix_site}_{problem_number}.py'

    make_dir(dir_path)
    make_file(file_path, url, cur_time_stamp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make template for BOJ problem solving')
    parser.add_argument('url', type=str, help='url of problem')
    parser.add_argument('--title', '-t', type=str, help='title of problem')
    args = parser.parse_args()

    if (args.title):
        print(args.title)
