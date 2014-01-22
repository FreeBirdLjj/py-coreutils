#!/usr/bin/env python3

import common
import getopt
import numpy
import os.path
import sys


def usage(prog):
    print("Usage: %s [OPTION]... [FILE]..." % prog)
    print("  or:  %s [OPTION]... --files0-from=F" % prog)
    print("Print newline, word, and byte counts for each FILE,",
          "and a total line if")
    print("more than one FILE is specified. ",
          "With no FILE, or when FILE is -,")
    print("read standard input. ",
          "A word is a non-zero-length sequence of characters")
    print("delimited by white space.")
    print("The options below may be used to select which counts are printed,",
          "always in")
    print("the following order:",
          "newline, word, character, byte, maximum line length.")
    print("  -c, --bytes           ",
          "print the byte counts")
    print("  -m, --chars           ",
          "print the character counts")
    print("  -l, --lines           ",
          "print the newline counts")
    print("      --files0-from=F   ",
          "read input from the files specified by")
    print("                          ",
          "NUL-terminated names in file F;")
    print("                          ",
          "If F is - then read names from standard input")
    print("  -L, --max-line-length ",
          "print the length of the longest line")
    print("  -w, --words           ",
          "print the word counts")
    pinrt("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("For complete documentation, run:",
          "info coreutils 'wc invocation'")


def wc(files, c=True, m=False, l=True, L=False, w=True):
    if files == []:
        f = sys.stdin
        lines = f.readlines()
        if l:
            lcnt = len(lines)
            print(" %d" % lcnt, end='')
        if w:
            wcnt = numpy.sum(list(map(lambda s: len(s.split()), lines)))
            print(" %d" % wcnt, end='')
        if m:
            ccnt = numpy.sum(list(map(len, lines)))
            print(" %d" % ccnt, end='')
        if c:
            bcnt = numpy.sum(list(map(lambda s: len(s.encode()), lines)))
            print(" %d" % bcnt, end='')
        if L:
            maxlno = lines.index(max(lines, key=lambda s: len(s.encode())))
            s = lines[maxlno].strip('\n').encode()
            lens = len(s)
            lenunansi = len(list(filter(lambda x: x >= 0x80, s)))
            maxl = lens - lenunansi / 3
            print(" %d" % maxl, end='')
        print()
    else:
        totall = totalw = totalm = totalc = totalL = 0
        for filename in files:
            if filename == "-":
                f = sys.stdin
            else:
                f = open(filename)
            lines = f.readlines()
            if l:
                lcnt = len(lines)
                totall += lcnt
                print(" %d" % lcnt, end='')
            if w:
                wcnt = numpy.sum(list(map(lambda s: len(s.split()), lines)))
                totalw += wcnt
                print(" %d" % wcnt, end='')
            if m:
                ccnt = numpy.sum(list(map(len, lines)))
                totalm += ccnt
                print(" %d" % ccnt, end='')
            if c:
                bcnt = os.path.getsize(filename)
                totalc += bcnt
                print(" %d" % bcnt, end='')
            if L:
                maxlno = lines.index(max(lines, key=lambda s: len(s.encode())))
                s = lines[maxlno].strip('\n').encode()
                lens = len(s)
                lenunansi = len(list(filter(lambda x: x >= 0x80, s)))
                maxl = lens - lenunansi / 3
                totalL = max(maxl, totalL)
                print(" %d" % maxl, end='')
            print(" %s" % filename)
        if len(files) > 1:
            if l:
                print(" %d" % totall, end='')
            if w:
                print(" %d" % totalw, end='')
            if m:
                print(" %d" % totalm, end='')
            if c:
                print(" %d" % totalc, end='')
            if L:
                print(" %d" % totalL, end='')
            print(" total")


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

    c = m = l = L = w = False
    if opts == []:
        l = w = c = True
    else:
        for op, value in opts:
            if op == "--help":
                usage(prog)
                exit(0)
            elif op == "--version":
                common.version(prog)
                exit(0)
            elif op == "-c" or op == "--bytes":
                c = True
            elif op == "-m" or op == "--chars":
                m = True
            elif op == "-l" or op == "--lines":
                l = True
            elif op == "-L" or op == "--max-line-length":
                L = True
            elif op == "-w" or op == "--words":
                w = True

    wc(args, c, m, l, L, w)
