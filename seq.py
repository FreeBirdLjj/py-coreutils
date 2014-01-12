#!/usr/bin/env python3

import common
import getopt
import re
import sys


def usage(prog):
    print("Usage: %s [OPTION]... LAST" % prog)
    print("  or:  %s [OPTION]... FIRST LAST" % prog)
    print("  or:  %s [OPTION]... FIRST INCREMENT LAST" % prog)
    print("Print numbers from FIRST to LAST, in steps of INCREMENT.")
    print()
    print("  -f, --format=FORMAT     ",
          "use printf style floating-point FORMAT")
    print("  -s, --separator=STRING  ",
          "use STRING to separate numbers (default: \\n)")
    print("  -w, --equal-width       ",
          "equalize width by padding with leading zeroes")
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("If FIRST or INCREMENT is omitted, it defaults to 1.  That is, an")
    print("omitted INCREMENT defaults to 1 even when LAST is smaller than FIRST.")
    print("FIRST, INCREMENT, and LAST are interpreted as floating point values.")
    print("INCREMENT is usually positive if FIRST is smaller than LAST, and")
    print("INCREMENT is usually negative if FIRST is greater than LAST.")
    print("FORMAT must be suitable for printing one argument of type 'double';")
    print("it defaults to %.PRECf if FIRST, INCREMENT, and LAST are all fixed point")
    print("decimal numbers with maximum precision PREC, and to %g otherwise.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'seq invocation'")


def argtonum(prog, arg):
    try:
        num = int(arg)
    except ValueError:
        try:
            num = float(arg)
        except ValueError:
            print("%s: invalid floating point argument: %s" % (prog, errarg),
                    file=sys.stderr)
            print("Try: '%s --help' for more information" % prog,
                    file=sys.stderr)
            exit(-1)
    return num


def seq(first, increment, last, fmt="%g", separator="\n", equalwidth=False):
    i = first
    while last <= i <= first or first <= i <= last:
        try:
            print(fmt % i, separator, end='')
        except TypeError:
            print("Error format string", file=stderr)
        i += increment

if __name__ == "__main__":
    prog = sys.argv[0]

    # FIXME: Can't resolve negative numbers.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:s:w",
                                   ["format=",
                                    "separator=",
                                    "equal-width",
                                    "help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)

    if opts == args == []:
        print("%s: missing operand" % prog, file=sys.stderr)
        print("Try 'seq --help' for more information", file=sys.stderr)
        exit(-1)
    if len(args) == 1:
        first = 1
        increment = 1
        last = argtonum(prog, args[0])
    elif len(args) == 2:
        first = argtonum(prog, args[0])
        increment = 1
        last = argtonum(prog, args[1])
    elif len(args) == 3:
        first = argtonum(prog, args[0])
        increment = argtonum(prog, args[1])
        last = argtonum(prog, args[2])
    else:
        print("%s: extra operand '%s'" % (prog, args[3]), file=sys.stderr)
        print("Try '%s --help' for more information" % prog, file=sys.stderr)
        exit(-1)

    fmt = "%g"
    separator = "\n"
    equalwidth = False

    for op, value in opts:
        if op == "-f" or op == "--format":
            fmt = value
        elif op == "-s" or op == "--separator":
            separator = value
        elif op == "-w" or op == "--equal-width":
            equalwidth = True
        elif op == "--help":
            usage(prog)
            exit(0)
        elif op == "--version":
            common.version(prog)
            exit(0)

    seq(first, increment, last, fmt, separator, equalwidth)