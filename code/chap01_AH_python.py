"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

def read_resp_file(dct_file="2002FemResp.dct", dat_file="2002FemResp.dat.gz"):
    # Using similar code as the ReadFemPreg from the textbook. Page 5 of the PDF version.
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    # Leaving out CleanFemPreg(df) as this doesn't seem to actually do anything.
    # The solution also just has 'pass' which indicates this function is incomplete/does not do anything.
    return df

resp = read_resp_file()

print(resp['pregnum'].value_counts().sort_index())
