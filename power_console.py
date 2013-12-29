# coding=utf-8
# -*- coding: utf-8 -*-

import sys

__author__ = 'nullexception'

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186


def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses

        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False


has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
    if sys.platform.startswith('win'):
        import ctypes
        from ctypes import windll, c_ulong
        windll.Kernel32.GetStdHandle.restype = c_ulong
        h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
        # for color in xrange(16):
        windll.Kernel32.SetConsoleTextAttribute(h, colour)
        sys.stdout.write(text.format(colour))
    else:
        if has_colours:
            seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
            sys.stdout.write(seq)
        else:
            sys.stdout.write(text)