#!/usr/bin/python3

import common
import getopt
import sys


def usage():
    print("""\
Usage: cat [OPTION]... [FILE]...
Concatenate FILE(s), or standard input, to standard output.

  -A, --show-all           equivalent to -vET
  -b, --number-nonblank    number nonempty output lines, overrides -n
  -e                       equivalent to -vE
  -E, --show-ends          display $ at end of each line
  -n, --number             number all output lines
  -s, --squeeze-blank      suppress repeated empty output lines
  -t                       equivalent to -vT
  -T, --show-tabs          display TAB characters as ^I
  -u                       (ignored)
  -v, --show-nonprinting   use ^ and M- notation, except for LFD and TAB
      --help     display this help and exit
      --version  output version information and exit

With no FILE, or when FILE is -, read standard input.

Examples:
  cat f - g  Output f's contents, then standard input, then g's contents.
  cat        Copy standard input to standard output.

For complete documentation, run: info coreutils 'cat invocation'\
""")


def printable(i):
    if i == 0:
        return '\0'
    if i >= 32:
        if i < 127:
            return chr(i)
        if i == 127:
            return "^?"
        if i >= 128 + 32:
            if i < 128 + 127:
                return "M-" + chr(i - 128)
            return "M-^?"
        return "M-^" + chr(i - 128 + 64)
    if i == ord('\t'):
        return "\t"
    if i == ord('\n'):
        pass
    else:
        return '^' + chr(i + 64)


def printablestr(str):
    sres = ""
    for ch in str:
        num = ch
        sres += printable(num >> 8) + printable(num & 0xFF)
    return sres


def cat(files, b=False, E=False, n=False, s=False, T=False, u=False, v=False):
    n |= b
    lineno = 0
    lastlineempty = False
    for fname in files:
        if fname == "-":
            f = sys.stdin
        else:
            try:
                f = open(fname, "r")
            except IOError:
                print("cat: %s: No such file or directory" % fname)
                exit(2)
        for line in f.readlines():
            newline = line[-1] == "\n"
            line = line.rstrip("\n")
            lineempty = line == ""
            if s and lastlineempty and lineempty:
                continue
            testb = b and lineempty
            lineno += 0 if testb else 1
            slineno = "%6d\t" % lineno if (n and not testb) else ""
            cend = "$" if E else ""
            if T:
                line = line.replace("\t", "^I")
            if v:
                line = line.encode("UTF-8")
                line = printablestr(line)
            LF = "\n" if newline else ""
            print("%s%s%s" % (slineno, line, cend), end=LF)
            lastlineempty = lineempty
        f.close()

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "AbeEnstTuv",
                                   ["show-all",
                                    "number-nonblank",
                                    "show-ends",
                                    "number",
                                    "squeeze-blank",
                                    "show-tabs",
                                    "show-nonprinting",
                                    "help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr("cat", wrngopt)
    b = E = n = s = T = u = v = False
    for op, value in opts:
        if op == "--help":
            usage()
            exit(0)
        elif op == "--version":
            common.version("cat")
            exit(0)
        elif op == "-A" or op == "--show-all":
            v = E = T = True
        elif op == "-b" or op == "--number-nonblank":
            b = True
        elif op == "-e":
            v = E = True
        elif op == "-E" or op == "--show-ends":
            E = True
        elif op == "-n" or op == "--number":
            n = True
        elif op == "-s" or op == "--squeze-blank":
            s = True
        elif op == "-t":
            v = T = True
        elif op == "-T" or op == "--show-tabs":
            T = True
        elif op == "-u":
            u = True
        elif op == "-v" or op == "--show-nonprinting":
            v = True
    cat(args, b, E, n, s, T, u, v)
    exit(0)
