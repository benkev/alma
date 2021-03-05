#
# diff_cal.py
#
#
#

import matplotlib.pyplot as plt
import numpy as np
import casacore.tables.table as castb
#import casacore.tables.tablecolumn as castc
import sys

scal1 = sys.argv[1]  # First calibration table file name
scal2 = sys.argv[2]  # Second calibration table file name

cal1 = castb(scal1)
cal2 = castb(scal2)

ncal1 = len(cal1)
ncal2 = len(cal2)
if ncal1 != ncal2:
    raise SystemExit('The CASA tables have different sizes, %d and %d' %
                     (ncal1, ncal2))
ncal = ncal1
ant1 = np.zeros(ncal, dtype=int)
ant2 = np.zeros(ncal, dtype=int)
dat1 = np.zeros(ncal, dtype=np.complex64)
dat2 = np.zeros(ncal, dtype=np.complex64)



for ix in range(ncal):
    ant1[ix] = cal1[ix]['ANTENNA1']
    ant2[ix] = cal1[ix]['ANTENNA1']
    dat1[ix] = cal1[ix]['CPARAM'][0,0]
    dat2[ix] = cal2[ix]['CPARAM'][0,0]

mag1 = np.abs(dat1)
mag2 = np.abs(dat2)
pha1 = np.degrees(np.angle(dat1))
pha2 = np.degrees(np.angle(dat2))

dmag = mag2 - mag1
dpha = pha2 - pha1

    



