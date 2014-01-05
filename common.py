#!/usr/bin/python3

def version(prog):
    print(prog, "0.0.1")

def opterr(prog, wrngopt):
    print("%s: invalid option --\'%s\'" %(prog, wrngopt.opt))
    print("Try \'%s --help\' for more information." %prog)
