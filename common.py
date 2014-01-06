#!/usr/bin/python3

import sys


def version(prog):
    print(prog, "0.0.1")


def opterr(prog, wrngopt):
    print("%s: invalid option --\'%s\'" % (prog, wrngopt.opt), file=sys.stderr)
    print("Try \'%s --help\' for more information." % (prog), file=sys.stderr)
    exit(-1)
