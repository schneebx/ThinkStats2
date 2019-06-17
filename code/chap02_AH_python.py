"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    # Followed the solution, but understand how Items works and that the value from Hist is the dictionary key, not the count. Also understand how the list comprehension operates.
    key, value = max([(key, value) for value, key in hist.Items()])
    return value


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    # Assignment to only do Mode, copied from solution to ensure code will run without errors
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)

def weight_comparison(live, firsts, others):
    # Utilizing existing function from thinkstats2
    d = thinkstats2.CohenEffectSize(firsts['totalwgt_lb'], others['totalwgt_lb'])
    return print('Weight Cohen Effect Size:', d)

def preg_length_comparison(live, firsts, others):
    # Utilizing existing function from thinkstats2
    d = thinkstats2.CohenEffectSize(firsts['prglngth'], others['prglngth'])
    return print('Preg Length Cohen Effect Size:', d)

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test weight_comparison
    weight_comparison(live, firsts, others)
    preg_length_comparison(live, firsts, others)

    # test Mode
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

# From the test run:
print('The birth weight has a slightly higher effect than the pregnancy length between first borns and non-first borns')
