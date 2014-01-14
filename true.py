#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s [ignored command line arguments]" % prog)
    print("  or:  %s OPTION" % prog)
    print("Exit with a status code indicating success.")
    print()
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("NOTE: your shell may have its own version of true,",
          "which usually supersedes")
    print("the version described here. ",
          "Please refer to your shell's documentation")
    print("for details about the options it supports.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'true invocation'")

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)

    if args != [] or len(opts) > 1:
        exit(0)
    op = opts[0][0]
    if op == "--help":
        usage(prog)
    elif op == "--version":
        common.version(prog)
