#!/usr/bin/env python3

import common
import getopt
import re
import sys


def usage(prog):
    print("Usage: %s [SHORT-OPTION]... [STRING]..." % prog)
    print("  or:  %s LONG-OPTION" % prog)
    print("Echo the STRING(s) to standard output.")
    print()
    print("  -n            ",
          "do not output the trailing newline")
    print("  -e            ",
          "enable interpretation of backslash escapes")
    print("  -E            ",
          "disable interpretation of backslash escapes (default)")
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("If -e is in effect, the following sequences are recognized:")
    print()
    print("  \\\\      backslash")
    print("  \\a      alert (BEL)")
    print("  \\b      backspace")
    print("  \\c      produce no further output")
    print("  \\e      escape")
    print("  \\f      form feed")
    print("  \\n      new line")
    print("  \\r      carriage return")
    print("  \\t      horizontal tab")
    print("  \\v      vertical tab")
    print("  \\0NNN   byte with octal value NNN (1 to 3 digits)")
    print("  \\xHH    byte with hexadecimal value HH (1 to 2 digits)")
    print()
    print("NOTE: your shell may have its own version of echo,",
          "which usually supersedes")
    print("the version described here. ",
          "Please refer to your shell's documentation")
    print("for details about the options it supports.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'echo invocation'")


def echo(strs, n=False, e=False):
    octdet = re.compile("\\\\0[0-7]{3}")
    hexdet = re.compile("\\\\x[\da-fA-F]{2}")
    ctoa = {'0': 0x0, '1': 0x1, '2': 0x2, '3': 0x3, '4': 0x4, '5': 0x5,
            '6': 0x6, '7': 0x7, '8': 0x8, '9': 0x9, 'A': 0xA, 'a': 0xA,
            'B': 0xB, 'b': 0xB, 'C': 0xC, 'c': 0xC, 'D': 0xD, 'd': 0xD,
            'E': 0xE, 'e': 0xE, 'F': 0xF, 'f': 0xF}
    escseq = (("\\\\", '\\'), ("\\a", '\a'), ("\\b", '\b'), ("\\e", '\033'),
              ("\\f", '\f'), ("\\n", '\n'), ("\\r", '\r'), ("\\t", '\t'),
              ("\\v", '\v'))
    endl = '' if n else '\n'
    for s in strs:
        if e:
            for c, escc in escseq:
                s = s.replace(c, escc)
            octdetres = re.findall(octdet, s)
            if octdetres != []:
                for octs in octdetres:
                    newc = chr(ctoa[octs[-1]] +
                               (ctoa[octs[-2]] << 3) +
                               (ctoa[octs[-3]] << 6))
                    s = s.replace(octs, newc)
            hexdetres = re.findall(hexdet, s)
            if hexdetres != []:
                for hexs in hexdetres:
                    newc = chr(ctoa[hexs[-1]] + (ctoa[hexs[-2]] << 4))
                    s = s.replace(hexs, newc)
            eofp = s.find("\\c")
            if eofp != -1:
                print(s[:eofp], end=endl)
                return
        print(s, end='')
    print(end=endl)


if __name__ == "__main__":
    prog = sys.argv[0]

    if len(sys.argv) == 2:
        op = sys.argv[1]
        if op == "--help":
            usage(prog)
            exit(0)
        if op == "--version":
            common.version(prog)
            exit(0)

    n = e = False
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-n":
            n = True
        elif sys.argv[i] == "-e":
            e = True
        elif sys.argv[i] == "-E":
            e = False
        else:
            echo(sys.argv[i:], n, e)
