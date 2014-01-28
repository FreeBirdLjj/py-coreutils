#!/usr/bin/env python3

import common
import getopt
import os
import sys


def usage(prog):
    print("Usage: %s [OPTION]... [VARIABLE]..." % prog)
    print("Print the values of the specified environment VARIABLE(s).")
    print("If no VARIABLE is specified,",
          "print name and value pairs for them all.")
    print()
    print("  -0, --null    ",
          "end each output line with 0 byte rather than newline")
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("NOTE: your shell may have its own version of printenv,"
          "which usually supersedes")
    print("the version described here. ",
          "Please refer to your shell's documentation")
    print("for details about the options it supports.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'printenv invocation'")

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "0",
                                   ["null",
                                    "help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)

    endc = '\n'
    for op, value in opts:
        if op == "--help":
            usage(prog)
            exit(0)
        elif op == "--version":
            common.version(prog)
            exit(0)
        elif op == "-0" or op == "--null":
            endc = '\0'

    if args == []:
        for k, v in os.environ.items():
            print("%s=%s" % (k, v), end=endc)
    else:
        for var in args:
            print("%s" % os.environ.get(var), end=endc)
