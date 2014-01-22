#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s [OPTION]... [FILE]..." % prog)
    print("  or:  %s [OPTION]... --files0-from=F" % prog)
    print("Print newline, word, and byte counts for each FILE, and a total line if")
    print("more than one FILE is specified.  With no FILE, or when FILE is -,")
    print("read standard input.  A word is a non-zero-length sequence of characters")
    print("delimited by white space.")
    print("The options below may be used to select which counts are printed, always in")
    print("the following order: newline, word, character, byte, maximum line length.")
    print("  -c, --bytes           ",
          "print the byte counts")
    print("  -m, --chars           ",
          "print the character counts")
    print("  -l, --lines           ",
          "print the newline counts")
    print("      --files0-from=F   ",
          "read input from the files specified by")
    print("                           NUL-terminated names in file F;")
    print("                           If F is - then read names from standard input")
    print("  -L, --max-line-length  print the length of the longest line")
    print("  -w, --words           ",
          "print the word counts")
    pinrt("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("For complete documentation, run:",
          "info coreutils 'wc invocation'")

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "cmlLw",
                                   ["bytes",
                                    "chars",
                                    "lines",
                                    "files0-from=",
                                    "max-line-length",
                                    "words",
                                    "help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)
