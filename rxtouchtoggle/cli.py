import sys
import argparse
from . import calc


def main():
    # arguments
    parser = argparse.ArgumentParser(description='')
    subparsers = parser.add_subparsers(help='')

    # commands.register('create', commands.create, subparsers)
    add_parser = subparsers.add_parser('add', help='add two integers')
    add_parser.set_defaults(cmd=calc.add)
    add_parser.add_argument("a", help="first integer (addend)")
    add_parser.add_argument("b", help="second integer (addend)")

    sub_parser = subparsers.add_parser('sub', help='subtract two integers')
    sub_parser.set_defaults(cmd=calc.sub)
    sub_parser.add_argument("a", help="first integer (minuend)")
    sub_parser.add_argument("b", help="second integer (subtrahend)")

    # parse args and execute command
    args = parser.parse_args()
    if hasattr(args, 'cmd'):
        print(args.cmd(int(args.a), int(args.b)))
        sys.exit()
    else:
        parser.print_help()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
