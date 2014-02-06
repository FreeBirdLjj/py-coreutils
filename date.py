#!/usr/bin/env python3

import common
import getopt
import sys


def usage(prog):
    print("Usage: %s [OPTION]... [+FORMAT]" % prog)
    print("  or:  %s [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]" % prog)
    print("Display the current time in the given FORMAT,",
          "or set the system date.")
    print()
    print("  -d, --date=STRING        ",
          "display time described by STRING, not \'now\'")
    print("  -f, --file=DATEFILE      ",
          "like --date once for each line of DATEFILE")
    print("  -I[TIMESPEC], --iso-8601[=TIMESPEC] ",
          "output date/time in ISO 8601 format.")
    print("                           ",
          "TIMESPEC=\'date\' for date only (the default),")
    print("                           ",
          "\'hours\', \'minutes\', \'seconds\', or \'ns\' for date")
    print("                           ",
          "and time to the indicated precision.")
    print("  -r, --reference=FILE     ",
          "display the last modification time of FILE")
    print("  -R, --rfc-2822           ",
          "output date and time in RFC 2822 format.")
    print("                           ",
          "Example: Mon, 07 Aug 2006 12:34:56 -0600")
    print("      --rfc-3339=TIMESPEC  ",
          "output date and time in RFC 3339 format.")
    print("                           ",
          "TIMESPEC=\'date\', \'seconds\', or \'ns\' for")
    print("                           ",
          "date and time to the indicated precision.")
    print("                           ",
          "Date and time components are separated by")
    print("                           ",
          "a single space: 2006-08-07 12:34:56-06:00")
    print("  -s, --set=STRING         ",
          "set time described by STRING")
    print("  -u, --utc, --universal   ",
          "print or set Coordinated Universal Time")
    print("      --help    ",
          "display this help and exit")
    print("      --version ",
          "output version information and exit")
    print()
    print("FORMAT controls the output. ",
          "Interpreted sequences are:")
    print()
    print("  %%  ",
          "a literal %")
    print("  %a  ",
          "locale\'s abbreviated weekday name (e.g., Sun)")
    print("  %A  ",
          "locale\'s full weekday name (e.g., Sunday)")
    print("  %b  ",
          "locale\'s abbreviated month name (e.g., Jan)")
    print("  %B  ",
          "locale\'s full month name (e.g., January)")
    print("  %c  ",
          "locale\'s date and time (e.g., Thu Mar  3 23:05:25 2005)")
    print("  %C  ",
          "century; like %Y, except omit last two digits (e.g., 20)")
    print("  %d  ",
          "day of month (e.g., 01)")
    print("  %D  ",
          "date; same as %m/%d/%y")
    print("  %e  ",
          "day of month, space padded; same as %_d")
    print("  %F  ",
          "full date; same as %Y-%m-%d")
    print("  %g  ",
          "last two digits of year of ISO week number (see %G)")
    print("  %G  ",
          "year of ISO week number (see %V); normally useful only with %V")
    print("  %h  ",
          "same as %b")
    print("  %H  ",
          "hour (00..23)")
    print("  %I  ",
          "hour (01..12)")
    print("  %j  ",
          "day of year (001..366)")
    print("  %k  ",
          "hour, space padded ( 0..23); same as %_H")
    print("  %l  ",
          "hour, space padded ( 1..12); same as %_I")
    print("  %m  ",
          "month (01..12)")
    print("  %M  ",
          "minute (00..59)")
    print("  %n  ",
          "a newline")
    print("  %N  ",
          "nanoseconds (000000000..999999999)")
    print("  %p  ",
          "locale\'s equivalent of either AM or PM; blank if not known")
    print("  %P  ",
          "like %p, but lower case")
    print("  %r  ",
          "locale\'s 12-hour clock time (e.g., 11:11:04 PM)")
    print("  %R  ",
          "24-hour hour and minute; same as %H:%M")
    print("  %s  ",
          "seconds since 1970-01-01 00:00:00 UTC")
    print("  %S  ",
          "second (00..60)")
    print("  %t  ",
          "a tab")
    print("  %T  ",
          "time; same as %H:%M:%S")
    print("  %u  ",
          "day of week (1..7); 1 is Monday")
    print("  %U  ",
          "week number of year, with Sunday as first day of week (00..53)")
    print("  %V  ",
          "ISO week number, with Monday as first day of week (01..53)")
    print("  %w  ",
          "day of week (0..6); 0 is Sunday")
    print("  %W  ",
          "week number of year, with Monday as first day of week (00..53)")
    print("  %x  ",
          "locale\'s date representation (e.g., 12/31/99)")
    print("  %X  ",
          "locale\'s time representation (e.g., 23:13:48)")
    print("  %y  ",
          "last two digits of year (00..99)")
    print("  %Y  ",
          "year")
    print("  %z  ",
          "+hhmm numeric time zone (e.g., -0400)")
    print("  %:z ",
          "+hh:mm numeric time zone (e.g., -04:00)")
    print("  %::z",
          " +hh:mm:ss numeric time zone (e.g., -04:00:00)")
    print("  %:::",
          "  numeric time zone with :",
          "to necessary precision (e.g., -04, +05:30)")
    print("  %Z  ",
          "alphabetic time zone abbreviation (e.g., EDT)")
    print()
    print("By default, date pads numeric fields with zeroes.")
    print("The following optional flags may follow \'%\':")
    print()
    print("  -  (hyphen) do not pad the field")
    print("  _  (underscore) pad with spaces")
    print("  0  (zero) pad with zeros")
    print("  ^  use upper case if possible")
    print("  #  use opposite case if possible")
    print()
    print("After any flags comes an optional field width,",
          "as a decimal number;")
    print("then an optional modifier, which is either")
    print("E to use the locale's alternate representations if available, or")
    print("O to use the locale's alternate numeric symbols if available.")
    print()
    print("Examples:")
    print("Convert seconds since the epoch (1970-01-01 UTC) to a date")
    print("  $ date --date=\'@2147483647\'")
    print()
    print("Show the time on the west coast of the US (use tzselect(1) to find TZ)")
    print("  $ TZ=\'America/Los_Angeles\' date")
    print()
    print("Show the local time for 9AM next Friday on the west coast of the US")
    print("  $ date --date=\'TZ=\"America/Los_Angeles\" 09:00 next Fri\'")
    print()
    print("For complete documentation, run:",
          "info coreutils \'date invocation\'")

if __name__ == "__main__":
    prog = sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:f:I:r:Rs:u",
                                   ["date=",
                                    "file=",
                                    "iso-8601=",
                                    "reference=",
                                    "rfc-2822",
                                    "rfc-3339=",
                                    "set=",
                                    "utc",
                                    "universal",
                                    "help",
                                    "version"])
    except getopt.GetoptError as wrngopt:
        common.opterr(prog, wrngopt)
