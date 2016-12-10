"""
Execute the solutions for a given day.

Usage: python aoc.py <day>

Example: python aoc.py day1
"""

import aoc2016

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print __doc__
        sys.exit(1)

    day = sys.argv[1]
    aoc2016.main(day)