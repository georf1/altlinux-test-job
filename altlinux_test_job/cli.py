import argparse


DESCRIPTION = 'Compares the resulting list of packages and shows a difference.'


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_branch', metavar='first_branch', type=str)
    parser.add_argument('second_branch', metavar='second_branch', type=str)
    parser.add_argument('output_file', metavar='output_file', type=str)

    return parser.parse_args()