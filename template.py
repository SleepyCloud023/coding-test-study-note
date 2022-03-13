import requests
import argparse
import os


def boj_make_dir(problem_number: int, url='Change this line to URL of Problem', category='./Greedy'):
    dir_path = f'{category}/boj_{problem_number}'
    file_path = f'{dir_path}/boj_{problem_number}.py'
    os.mkdir(f'{category}/boj_{problem_number}')
    with open(file_path, 'w') as fp:
        fp.write(f'# {url}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make template for BOJ problem solving')
    parser.add_argument('url', type=str, help='url of problem')
    parser.add_argument('--title', '-t', type=str, help='title of problem')
    args = parser.parse_args()

    if (args.title):
        print(args.title)
