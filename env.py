#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s [OPTION]... [-] [NAME=VALUE]... [COMMAND [ARG]...]" % prog)
    print("Set each NAME to VALUE in the environment and run COMMAND.")
    print()
    print("  -i, --ignore-environment ",
          "start with an empty environment")
    print("  -0, --null          ",
          "end each output line with 0 byte rather than newline")
    print("  -u, --unset=NAME    ",
          "remove variable from the environment")
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("A mere - implies -i. ",
          "If no COMMAND, print the resulting environment.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'env invocation'")

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i0u:",
                                   ["ignore-environment",
                                    "null",
                                    "unset=",
                                    "help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)
