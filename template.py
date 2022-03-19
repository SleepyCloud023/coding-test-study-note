import requests
import argparse
import os
import time
import re
from bs4 import BeautifulSoup
import cfscrape
#import requests

# Current supported
# https://www.acmicpc.net
# https://programmers.co.kr


supported_url = {'acmicpc': ('id', 'problem_title'),
                 'programmers': ('class', 'algorithm-title')}


def make_template(prefix_site: str, url: str, category: str, title: str = '', update=False):
    cur_time = time.localtime()
    cur_time_stamp = time.strftime('%Y-%m-%d %I:%M:%S %p', cur_time)

    title, problem_number = get_info_from_url(url, title)
    dir_path = f'{category}/{prefix_site}_{problem_number}'
    file_path = f'{dir_path}/{prefix_site}_{problem_number}.py'

    make_dir(dir_path, update)
    make_file(file_path, url, cur_time_stamp, title)


def get_info_from_url(url: str, title: str) -> str:
    if title == '':
        title = get_title_text(url)

    number = extract_number(url)

    return title, number


def get_title_text(url: str) -> str:
    title_text = ''
    # NOTE: BOJ 페이지 => requests 라이브러리 get 메소드 사용시 403 status 반환
    scraper = cfscrape.create_scraper()
    problem_page = scraper.get(url).content
    soup = BeautifulSoup(problem_page, 'html.parser')

    domain_name = get_domain_name(url)

    if domain_name == -1:
        return ''

    selector_type, selector_value = get_title_selector(domain_name)

    if selector_type == 'id':
        title_tag = soup.find(id=selector_value)

    elif selector_type == 'class':
        title_tag = soup.find(class_=selector_value)

    else:
        raise ValueError(f'unsupported selector type : {selector_type}')

    title_text = title_tag.text.strip()
    return title_text


def get_domain_name(url: str) -> str:
    domain_match_object = re.match(
        r'.*//(www[.])?(?P<domain>[a-z]+)[.].*', url)
    domain_name = -1

    if domain_match_object:
        domain_matched = domain_match_object.group('domain')

        if domain_matched in supported_url:
            domain_name = domain_matched

    return domain_name


def get_title_selector(domain_name: str) -> str:
    if domain_name in supported_url:
        return supported_url[domain_name]
    else:
        raise ValueError('unsupported site type')


def extract_number(url: str) -> str:
    number_match_object = re.match(r'.*/([\d_]+)$', url)

    if number_match_object:
        number = number_match_object.group(1)
        return number

    else:
        raise ValueError('can not find problem number')


def make_dir(dir_path: str, update: bool):
    try:
        os.mkdir(dir_path)
    except:
        print(
            '*' * 12, f'target directory already exists: "{dir_path}"', '*' * 12)

        if update == False:
            raise ValueError(
                f'delete previous directory or add update parameter to force update')
        else:
            print('update internale source file')


def make_file(file_path: str, url: str, cur_time_stamp: str, title):
    with open(file_path, 'w', encoding='utf-8') as fp:
        fp.write(f'# {url}\n')
        fp.write(f'# title: {title}\n')
        fp.write(f'# start: {cur_time_stamp}\n')
        fp.write(f'# end:   {cur_time_stamp}\n')


# TODO: cli 인터페이스 제공
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make template for problem solving')
    parser.add_argument('url', type=str, help='url of problem')
    parser.add_argument('--title', '-t', type=str, help='title of problem')
    args = parser.parse_args()

    if (args.title):
        print(args.title)
