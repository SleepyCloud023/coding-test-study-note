import requests
import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make template for BOJ problem solving')
    parser.add_argument('url', type=str, help='url of problem')
    parser.add_argument('--title', '-t', type=str, help='title of problem')
    args = parser.parse_args()

    if (args.title):
        print(args.title)
