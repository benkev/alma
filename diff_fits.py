'''
Compare two image fits file datacubes
'''
import numpy as np
import astropy.io.fits as pf 
import os, platform

hostname = platform.node()   # Host name
hostname = hostname.split('.')[0]

#
# Make this script running universally on our several machines.
# The "home" directory (supposedly containing the ALMA and smili2_dev
# directories) is different on different servers.
# On leonid2 and capelin (Lynn) it is
#     /data-smili/smili2_dev
# On isco it is
#     /data-smili
# On my machine it is my home directory, ~ = /home/benkev
#
#
if hostname == 'isco':
    homedir = '/data-isco/data-smili/'
elif hostname == 'leonid2' or hostname == 'capelin':
    homedir = '/data-smili/'
else:
    homedir = os.path.expanduser('~') + '/'
    
basedir = homedir + 'ALMA/'


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
    





