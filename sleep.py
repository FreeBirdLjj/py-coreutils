#!/usr/bin/env python3

import common
import getopt
import sys
import time


def usage(prog):
    print("Usage: %s NUMBER[SUFFIX]..." % prog)
    print("  or:  %s OPTION" % prog)
    print("Pause for NUMBER seconds. ",
          "SUFFIX may be 's' for seconds (the default),")
    print("'m' for minutes, 'h' for hours or 'd' for days. ",
          "Unlike most implementations")
    print("that require NUMBER be an integer,",
          "here NUMBER may be an arbitrary floating")
    print("point number. ",
          "Given two or more arguments, pause for the amount of time")
    print("specified by the sum of their values.")
    print()
    print("      --help     display this help and exit")
    print("      --version  output version information and exit")
    print()
    print("For complete documentation, run:",
          "info coreutils 'sleep invocation'")


def sleep(sec):
    time.sleep(sec)


def argtonum(prog, arg):
    try:
        t = float(arg)
    except ValueError:
        print("%s: invalid time interval '%s'" % (prog, arg),
              file=sys.stderr)
        print("Try '%s --help' for more information." % prog,
              file=sys.stderr)
        exit(-1)
    return t


if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)

    if args == [] and opts == []:
        print("%s: missing operand" % prog, file=sys.stderr)
        print("Try '%s --help' for more information." % prog, file=sys.stderr)
        exit(-1)

    if opts != []:
        if len(sys.argv) > 2:
            common.opterr(prog, getopt.GetoptError(None, opt="-"))
        op = opts[0][0]
        if op == "--help":
            usage(prog)
        elif op == "version":
            common.version(prog)

    for arg in args:
        scala = 1
        if arg[-1] == 's':
            t = argtonum(prog, arg[:-1])
        elif arg[-1] == 'm':
            scala = 60
            t = argtonum(prog, arg[:-1])
        elif arg[-1] == 'h':
            scala = 3600
            t = argtonum(prog, arg[:-1])
        elif arg[-1] == 'd':
            scala = 86400
            t = argtonum(prog, arg[:-1])
        else:
            t = argtonum(prog, arg)
        t *= scala
        sleep(t)
