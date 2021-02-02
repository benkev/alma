'''
Compare two image fits file datacubes
'''
import numpy as np
import astropy.io.fits as pf 
from alma_util import workdir

#
# Make this script running universally on our several machines.
#  
basedir = workdir() + 'ALMA/'

fits1 = basedir + 'RoundSpottyDisk.fits'
fits2 = basedir + 'RoundSpottyDisk_smili.fits'

hdu1 = pf.open(fits1)[0]
dat1 = np.asarray(hdu1.data[0,0]) 

hdu2 = pf.open(fits2)[0]
dat2 = np.asarray(hdu2.data[0,0]) 

if np.any(abs(dat1 - dat2) == 0.):
    print('Data in', fits1, 'and', fits2, 'are identical.')
else:
    print('Data in', fits1, 'and', fits2, 'are different.')
    





