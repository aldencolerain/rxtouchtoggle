import sys
import argparse
from . import toggle


def main():
    # arguments
    parser = argparse.ArgumentParser(description='')
    subparsers = parser.add_subparsers(help='')

    # start toggle command
    add_parser = subparsers.add_parser('start', help='start touche toggle tray widget')
    add_parser.set_defaults(cmd=toggle.start)

    # parse args and execute command
    args = parser.parse_args()
    if hasattr(args, 'cmd'):
        args.cmd()
        sys.exit()
    else:
        parser.print_help()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
