#!/usr/bin/env python3

import common
import getopt
import os
import os.path
import sys


def usage(prog):
    print("Usage: %s [OPTION] NAME..." % prog)
    print("Output each NAME with its last non-slash component and trailing slashes")
    print("removed;",
          "if NAME contains no /'s,",
          "output '.' (meaning the current directory).")
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
    print("For complete documentation, run:",
          "info coreutils 'dirname invocation'")


def dirname(paths):
    def _dirname(path):
        result = os.path.dirname(path)
        return "." if result == "" else result
    return map(_dirname, paths)

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "z",
                                   ["help",
                                    "version",
                                    "zero"])
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
        elif op == "-z" or op == "--zero":
            endc = ''

    if args == []:
        common.missop(prog)

    for s in dirname(args):
        print(s, end=endc)
