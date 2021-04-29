#!/usr/bin/env python3

from subprocess import run
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("message", nargs='+')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--feature', '-f', action='store_true', help="mark the commit as a feature")
    group.add_argument('--bug', '-b', action='store_true', help="mark the commit as a bug fix")
    group.add_argument('--documentation', '-d', action='store_true', help="mark the commit as a documentation change")
    group.add_argument('--refactor', '-r', action='store_true', help="mark the commit as a code refactor")
    group.add_argument('--chore', '-c', action='store_true', help="mark the commit as a operations change")

    arguments = parser.parse_args()
    message = ' '.join(arguments.message)

    if arguments.feature:
        message = 'feature: ' + message
    elif arguments.bug:
        message = 'bug: ' + message
    elif arguments.documentation:
        message = 'doc: ' + message
    elif arguments.refactor:
        message = 'refactor: ' + message
    elif arguments.chore:
        message = 'chore: ' + message

    run(['git', 'commit', '-m', message])


if __name__ == '__main__':
    main()
