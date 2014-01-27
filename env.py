#!/usr/bin/env python3

import common
import functools
import getopt
import os
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

    endc = '\n'
    for op, value in opts:
        if op == "--help":
            usage(prog)
            exit(0)
        elif op == "--version":
            common.version(prog)
            exit(0)
        elif op == "-i" or op == "--ignore-environment":
            os.environ.clear()
        elif op == "-0" or op == "--null":
            endc = '\0'
        elif op == "-u" or op == "--unset":
            try:
                os.environ.pop(value)
            except KeyError:
                pass
    
    if args == []:
        for k, v in os.environ.items():
            print("%s=%s" % (k, v), end=endc)
    else:
        for i in range(len(args)):
            eql = args[i].find('=')
            if eql == -1:
                continue
            os.putenv(args[i][:eql], args[i][eql+1:])
            del args[i]
        os.execvp(args[0], args)
