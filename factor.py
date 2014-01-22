#!/usr/bin/env python3

import common
import getopt
import math
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
    print("For complete documentation, run:",
          "info coreutils 'factor invocation'")


def factor(num):
    result = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num //= i
            result.append(i)
    if num > 1:
        result.append(num)
    return result


def factorstr(prog, nums):
    if nums == []:
        try:
            while True:
                s = input()
                nums = re.split("\\s+", s)
                for num in nums:
                    try:
                        i = int(num)
                        print("%d:" % i, end='')
                        result = factor(i)
                        list(map(lambda j: print(" %d" % j, end=''), result))
                        print()
                    except ValueError:
                        print("%s: '%s' is not a valid positive integer"
                              % (prog, num))
        except EOFError:
            pass
    else:
        for num in nums:
            try:
                i = int(num)
                print("%d:" % i, end='')
                result = factor(i)
                list(map(lambda j: print(" %d" % j, end=''), result))
                print()
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
