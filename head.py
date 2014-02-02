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
