#!/usr/bin/env python3

import common
import getopt
import re
import sys

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

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


def dirname(paths):
    def _dirname(path):
        lastslash = path.rfind('/')
        if lastslash == -1:
            return '.'
        else:
            return path[:lastslash]
    pool = ThreadPool()
    result = pool.map(_dirname, paths)
    pool.close()
    pool.join()
    return result

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
    for op, value in opts:
        if op == "--help":
            usage(prog)
            exit(0)
        elif op == "--version":
            common.version(prog)
            exit(0)
        elif op == "-z" or op == "--zero":
            z = True

    if args == []:
        print("%s: missing operand" % prog)
        print("Try '%s --help' for more information" % prog)
    else:
        for s in dirname(args):
            if z:
                print(s, end='')
            else:
                print(s)
