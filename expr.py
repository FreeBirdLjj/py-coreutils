#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s EXPRESSION" % prog)
    print("  or:  %s OPTION" % prog)
    print()
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("Print the value of EXPRESSION to standard output. ",
          "A blank line below")
    print("separates increasing precedence groups. ",
          "EXPRESSION may be:")
    print()
    print("  ARG1 | ARG2      ",
          "ARG1 if it is neither null nor 0, otherwise ARG2")
    print()
    print("  ARG1 & ARG2      ",
          "ARG1 if neither argument is null or 0, otherwise 0")
    print()
    print("  ARG1 < ARG2      ",
          "ARG1 is less than ARG2")
    print("  ARG1 <= ARG2     ",
          "ARG1 is less than or equal to ARG2")
    print("  ARG1 = ARG2      ".
          "ARG1 is equal to ARG2")
    print("  ARG1 != ARG2     ",
          "ARG1 is unequal to ARG2")
    print("  ARG1 >= ARG2     ",
          "ARG1 is greater than or equal to ARG2")
    print("  ARG1 > ARG2      ",
          "ARG1 is greater than ARG2")
    print()
    print("  ARG1 + ARG2      ",
          "arithmetic sum of ARG1 and ARG2")
    print("  ARG1 - ARG2      ",
          "arithmetic difference of ARG1 and ARG2")
    print()
    print("  ARG1 * ARG2      ",
          "arithmetic product of ARG1 and ARG2")
    print("  ARG1 / ARG2      ",
          "arithmetic quotient of ARG1 divided by ARG2")
    print("  ARG1 %% ARG2      ",
          "arithmetic remainder of ARG1 divided by ARG2")
    print()
    print("  STRING : REGEXP  ",
          "anchored pattern match of REGEXP in STRING")
    print()
    print("  match STRING REGEXP       ",
          "same as STRING : REGEXP")
    print("  substr STRING POS LENGTH  ",
          "substring of STRING, POS counted from 1")
    print("  index STRING CHARS        ",
          "index in STRING where any CHARS is found, or 0")
    print("  length STRING             ",
          "length of STRING")
    print("  + TOKEN                   ",
          "interpret TOKEN as a string, even if it is a")
    print("                            ",
          "  keyword like \'match\' or an operator like \'/\'")
    print()
    print("  ( EXPRESSION )            ",
          "value of EXPRESSION")
    print()
    print("Beware that many operators need to be escaped or quoted for shells.")
    print("Comparisons are arithmetic if both ARGs are numbers, else lexicographical.")
    print("Pattern matches return the string matched between \\( and \\) or null; if")
    print("\\( and \\) are not used, they return the number of characters matched or 0.")
    print()
    print("Exit status is 0 if EXPRESSION is neither null nor 0, 1 if EXPRESSION is null")
    print("or 0, 2 if EXPRESSION is syntactically invalid, and 3 if an error occurred.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'expr invocation'")

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)

    for op, value in opts:
        if op == "--help":
            usage(prog)
            exit(0)
        elif op == "--version":
            common.version(prog)
            exit(0)

    for i in range(len(args)):
        pass
