#!/usr/bin/env python3

import common
import getopt
import re
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
    print("  ARG1 = ARG2      ",
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
    print("  ARG1 % ARG2      ",
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
    print("Comparisons are arithmetic if both ARGs are numbers,",
          "else lexicographical.")
    print("Pattern matches return the string matched between \\( and \\) or null; if")
    print("\\( and \\) are not used,",
          "they return the number of characters matched or 0.")
    print()
    print("Exit status is 0 if EXPRESSION is neither null nor 0,",
          "1 if EXPRESSION is null")
    print("or 0,",
          "2 if EXPRESSION is syntactically invalid,",
          "and 3 if an error occurred.")
    print()
    print("For complete documentation, run:",
          "info coreutils 'expr invocation'")


def expr(exprs):
    """
    exprs should be a list of string, and is not [].
    """

    test_match = re.compile(r".*\\\(.*\\\).*")

    def expr_match(string, pattern):
        nonlocal test_match
        if test_match.match(pattern) is None:
            """
            return a string which means the length of matched substring
            """
            pattern = pattern.replace("(", "\\(").replace(")", "\\)")
            matches = re.match(pattern, string)
            return "0" if matches is None else str(len(matches.group()))
        else:
            """
            return the (last?) matched substring
            """
            pattern = pattern.replace("\\(", "(").replace("\\)", ")")
            matches = re.match(pattern, string)
            return "" if matches is None else matches.groups()[0]

    def getstr():
        if exprs == []:
            raise SyntaxError
        if exprs[0] == "+":
            if len(exprs) == 1:
                raise SyntaxError
            string = exprs[1]
            del exprs[:2]
            return string
        string = exprs[0]
        del exprs[0]
        return string

    if len(exprs) == 1:
        return exprs[0]
    if exprs[0] == "(":
        rparen = -1
        for i in range(len(exprs)):
            if exprs[i] == ")":
                rparen = i
        subexprs = exprs[1:rparen]
        del exprs[:rparen + 1]
        exprs.insert(0, expr(subexprs))
        return expr(exprs)
    elif exprs[0] == ")":
        raise SyntaxError
    elif exprs[0] == "match":
        del exprs[0]
        string = getstr()
        pattern = getstr()
        exprs.insert(0, expr_match(string, pattern))
        return expr(exprs)
    elif exprs[0] == "substr":
        del exprs[0]
        string = getstr()
        strlen = len(string)
        try:
            pos = int(getstr())
            length = int(getstr())
        except ValueError:
            exprs.insert(0, "")
            return expr(exprs)
        if pos < 1:
            raise SyntaxError
        pos -= 1
        substr = string[pos:pos + length]
        exprs.insert(0, substr)
        return expr(exprs)
    elif exprs[0] == "index":
        del exprs[0]
        string = getstr()
        chars = getstr()
        pattern = "[" + chars + "]"
        result = re.compile(pattern).search(string)
        if result is None:
            exprs.insert(0, "0")
        else:
            exprs.insert(0, str(result.start() + 1))
        return expr(exprs)
    elif exprs[0] == "length":
        del exprs[0]
        string = getstr()
        exprs.insert(0, str(len(string)))
        return expr(exprs)
    else:
        arg1 = getstr()
        if exprs == []:
            exprs = [arg1]
            return expr(exprs)
        op = exprs[0]
        del exprs[0]
        arg2 = getstr()
        if op == "+":
            result = int(arg1) + int(arg2)
        elif op == "-":
            result = int(arg1) - int(arg2)
        elif op == "*":
            result = int(arg1) * int(arg2)
        elif op == "/":
            result = int(arg1) / int(arg2)
        elif op == "%":
            result = int(arg1) % int(arg2)
        elif op == ":":
            result = expr_match(arg1, arg2)
        else:
            raise SyntaxError
        exprs.insert(0, str(result))
        return expr(exprs)


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

    if args == []:
        common.missop(prog)
    try:
        result = expr(args)
        print(result)
    except SyntaxError:
        print("%s: syntax error" % prog)
        exit(2)
    except ValueError or TypeError:
        print("%s: non-integer argument" % prog)
        exit(2)

    if result == "" or result == "0":
        exit(1)
