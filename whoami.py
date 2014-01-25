#!/usr/bin/env python3

import common
import getopt
import getpass
import sys


def usage(prog):
    print("Usage: %s [OPTION]..." % prog)
    print("Print the user name associated with the current effective user ID.")
    print("Same as id -un.")
    print()
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("For complete documentation, run:",
          "info coreutils 'whoami invocation'")


def whoami():
    return getpass.getuser()


if __name__ == "__main__":
    prog = sys.argv[0]
    try:
        opts, args = getopt.getopt(sys.argv[1:], "",
                                   ["help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)
    if args != []:
        common.extraop(prog, args[0])
    if len(opts) > 1:
        wrngopt = getopt.GetoptError(None, '-')
        common.opterr(prog, wrngopt)
    if opts == []:
        print(whoami())
    else:
        op, value = opts[0]
        if value != '':
            wrngopt = getopt.GetoptError(None, '-')
            common.opterr(prog, wrngopt)
        elif op == "--help":
            usage(prog)
        elif op == "--version":
            common.version(prog)
