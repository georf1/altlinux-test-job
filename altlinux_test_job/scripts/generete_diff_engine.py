#!/usr/bin/env python
from altlinux_test_job.cli import parse_args
from altlinux_test_job.get_diff_engine import generate_diff


def main():
    args = parse_args()
    generate_diff(args.first_branch, args.second_branch, args.output_file)
    print('The file was successfully written')


if __name__ == '__main__':
    main()
