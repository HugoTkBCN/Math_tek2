#!/usr/bin/python3

import sys

def is_numeric_args(args):
    for argument in args[1:]:
        if (not argument.isdigit()):
            return False
    return True

def print_usage():
    print("USAGE")
    print("\t./202unsold a b")
    print("DESCRIPTION")
    print("\ta\tconstant computed from past results")
    print("\tb\tconstant computed from past results")

def check_args():
    ac = len(sys.argv)
    if (ac == 2 and sys.argv[1] == "-h"):
        print_usage()
        exit(0)
    if (not is_numeric_args(sys.argv) or ac != 3
        or (int(sys.argv[1]) < 50 or int(sys.argv[1]) > 100)
        or (int(sys.argv[2]) < 50 or int(sys.argv[2]) > 100)):
        exit(84)
