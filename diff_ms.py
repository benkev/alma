#
# diff_ms.py
#
# Compare the visibility data from simulated observations of a Betelgeuse sky
# image created in CASA with the same image after loading to SMILI2 and
# saving. 
#

import matplotlib.pyplot as plt
import numpy as np
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


msn1 = basedir + 'alma/alma.alma.cycle7.10.ms'              # Created in CASA
msn2 = basedir + 'alma_smili/alma_smili.alma.cycle7.10.ms/' # Saved from SMILI2

cols = ['antenna1', 'antenna2', 'u', 'v', 'w', 'data',
                         'flag', 'flag_row']

#
# Read in dat1 the visibilities of the image created with CASA
#
ms.open(msn1, nomodify=True)
ms.selectinit(datadescid=0)      # Reset all previous selections

rec = ms.getdata(cols)
dat1 = np.squeeze(rec['data'])

ms.close()

#
# Read in dat2 the visibilities of the same image after loading/saving
# in SMILI2
#
ms.open(msn2, nomodify=True)
ms.selectinit(datadescid=0)      # Reset all previous selections

rec = ms.getdata(cols)
dat2 = np.squeeze(rec['data'])

ms.close()

#
# Comparison
#

#
# Absolute value of the difference are large
#
dif = np.abs(dat2 - dat1)      # dif = |dat2 - dat1|
dif = dif[0]   # The polarizations (?) are the same, so leave only one

#
# Absolute values before and after SMILI2
#
absd1 = np.abs(dat1[0])
absd2 = np.abs(dat2[0])
abs_dif_abs = np.abs(absd2 - absd1)

print('max(abs_dif_abs) = ', max(abs_dif_abs))

if np.any(abs(absd1 - absd2) == 0.):
    print('Data in', msn, 'and', msn2, 'are identical.')
else:
    print('Data in', msn1, 'and', msn2, 'are different.')

ph = np.angle(dat2 - dat1)[0]

plt.figure(); plt.plot(ph); plt.grid(1) 





        
