#!/usr/bin/env python3

import common
import getopt
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

if __name__ == "__main__":
    prog = sys.argv[0]
