#!/usr/bin/env python3

import common
import getopt
import re
import sys


def usage(prog):
    print("Usage: %s [NUMBER]..." % prog)
    print("  or:  %s OPTION" % prog)
    print("Print the prime factors of each specified integer NUMBER.  If none")
    print("are specified on the command line, read them from standard input.")
    print()
    print("      --help     display this help and exit")
    print("      --version  output version information and exit")
    print()
    print("For complete documentation, run: info coreutils 'factor invocation'")


def factor(num):
    print("%d:" % num, sep='', end='')
    i = 2
    while i * i <= num:
        if num % i == 0:
            print(" %d" % i, sep='', end='')
            num //= i
        i += 1
    if num > 1:
        print(" %d" % num, sep='')


def factorstr(prog, nums):
    if nums == []:
        try:
            while True:
                s = input()
                nums = re.split("\s+", s)
                for num in nums:
                    try:
                        i = int(num)
                        factor(i)
                    except ValueError:
                        print("%s: '%s' is not a valid positive integer" % (prog, num))
        except EOFError:
            pass
    else:
        for num in nums:
            try:
                i = int(num)
                factor(i)
            except ValueError:
                print("%s: '%s' is not a valid positive integer" % (prog, num))


if __name__ == "__main__":
    prog = sys.argv[0]
    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)
    if opts == []:
        factorstr(prog, args)
    else:
        op = opts[0][0]
        if op == "--help":
            usage(prog)
        elif op == "--version":
            common.version(prog)
