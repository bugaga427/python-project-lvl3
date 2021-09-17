import argparse
import os


def generate_parser():
    parser = argparse.ArgumentParser(
        prog='page-loader',
        usage='%(prog)s [options] <url>',
        description='PageLoader is a command \
        line utility that downloads pages from \
        the Internet and stores them on your computer.'
    )
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help='output dir (default: current directory)')
    parser.add_argument('url')
    args = parser.parse_args()
    return args
