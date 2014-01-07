#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s [STRING]..." % prog)
    print("  or:  %s OPTION" %prog)
    print("Repeatedly output a line with all specified STRING(s), or 'y'.")
    print()
    print("      --help     display this help and exit")
    print("      --version  output version information and exit")
    print()
    print("For complete documentation, run: info coreutils 'yes invocation'")


def yes(strs):
    pass


if __name__ == "__main__":
    prog = sys.argv[0]
    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)
    if opts == []:
        yes(args)
    if len(opts) > 1 or args != []:
        wrngopt = getopt.GetoptError(None, '-')
        common.opterr(prog, wrngopt)
