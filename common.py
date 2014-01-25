import sys


def version(prog):
    print(prog, "0.0.1")


def opterr(prog, wrngopt):
    print("%s: invalid option --\'%s\'" % (prog, wrngopt.opt), file=sys.stderr)
    print("Try \'%s --help\' for more information." % (prog), file=sys.stderr)
    exit(1)


def ferr(prog, file):
    print("%s: %s: No such file or directory" % (prog, file), file=sys.stderr)
    exit(2)

def missop(prog):
    print("%s: missing operand" % (prog), file=sys.stderr)
    print("Try \'%s --help\' for more information." % (prog), file=sys.stderr)
    exit(1)
