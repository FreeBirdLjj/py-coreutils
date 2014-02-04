#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s [OPTION]... [FILE]..." % prog)
    print("Print the first 10 lines of each FILE to standard output.")
    print("With more than one FILE, precede each with a header giving the file name.")
    print("With no FILE, or when FILE is -, read standard input.")
    print()
    print("Mandatory arguments to long options are mandatory for short options too.")
    print("  -c, --bytes=[-]K        ",
          "print the first K bytes of each file;")
    print("                            ",
          "with the leading '-', print all but the last")
    print("                            ",
          "K bytes of each file")
    print("  -n, --lines=[-]K        ",
          "print the first K lines instead of the first 10;")
    print("                            ",
          "with the leading '-', print all but the last")
    print("                            ",
          "K lines of each file")
    print("  -q, --quiet, --silent   ",
          "never print headers giving file names")
    print("  -v, --verbose           ",
          "always print headers giving file names")
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("K may have a multiplier suffix:")
    print("b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,")
    print("GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'head invocation'")


def str2size(s: str):
    size_scale = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    try:
        if s.isdigit():
            return int(s)
        elif s[-2].isdigit():
            return int(s[-1]) * (1024 ** size_scale.index(s[-1]))
        elif s[-1] != 'B':
            raise SyntaxError
        return int(s[-2]) * (1000 ** size_scale.index(s[-1]))
    except (IndexError, ValueError):
        raise SyntaxError


def head(filenames: list of str, by_line: bool, k: int, v: bool):
    return []

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:n:qv",
                                   ["bytes=",
                                    "lines=",
                                    "quiet",
                                    "silent",
                                    "verbose",
                                    "help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)

    by_line = True
    k = 10
    v = True
    for op, value in opts:
        if op == "--help":
            usage(prog)
            exit(0)
        elif op == "--version":
            common.version(prog)
            exit(0)
        elif op == "-c" or op == "--bytes":
            by_line = False
            k = str2size(value)
        elif op == "-n" or op == "--lines":
            by_line = True
            k = str2size(value)
        elif op == "-q" or op == "--quiet" or op == "--silent":
            v = False
        elif op == "-v" or op == "--verbose":
            v = True

    try:
        for line in head(args, by_line, k, v):
            print(line)
    except:
        pass
