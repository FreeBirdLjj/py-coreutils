#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s [OPTION] NAME..." % prog)
    print("Output each NAME with its last non-slash component and trailing slashes")
    print("removed; if NAME contains no /'s, output '.' (meaning the current directory).")
    print()
    print("  -z, --zero    ",
          "separate output with NUL rather than newline")
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("Examples:")
    print("  dirname /usr/bin/          -> \"/usr\"")
    print("  dirname dir1/str dir2/str  -> \"dir1\" followed by \"dir2\"")
    print("  dirname stdio.h            -> \".\"")
    print()
    print("For complete documentation, run: info coreutils 'dirname invocation'")


if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "z",
                                   ["help",
                                    "version",
                                    "zero"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)

    z = False
