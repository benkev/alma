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
dat1 = np.squeeze(rec['data'])   # Through away zero-length dimensions

ms.close()

#
# Read in dat2 the visibilities of the same image after loading/saving
# in SMILI2
#
ms.open(msn2, nomodify=True)
ms.selectinit(datadescid=0)      # Reset all previous selections

rec = ms.getdata(cols)
dat2 = np.squeeze(rec['data'])   # Through away zero-length dimensions

ms.close()

#
# Comparison
#

#
# The data in two polarization channels, XX and YY, are equal, so we only
# leave one: 
#
dat1 = dat1[0]
dat2 = dat2[0]

#
# Absolute value of the difference are large
#
dif = np.abs(dat2 - dat1)      # dif = |dat2 - dat1|

#
# Absolute values before and after SMILI2
#
absd1 = np.abs(dat1)
absd2 = np.abs(dat2)
abs_dif_abs_dat12 = np.abs(absd2 - absd1)

print('max( ||dat2| - |dat1|| ) = %e' % max(abs_dif_abs_dat12))


#
# Plot phases before and after SMILI2 along with their difference
#
radeg = 180/np.pi
ph1 = np.angle(dat1)
ph2 = np.angle(dat2)
dif_ph = ph2 - ph1

npt = 130                         # Only plot first npt points
tim = np.arange(npt)

fig, ax = plt.subplots()           # Create new figure fig with axes ax

ax.plot(dif_ph[:npt]*radeg, 'r', lw=2, label='Phase difference')
ax.plot(ph1[:npt]*radeg, 'b', label='Phase original')
ax.plot(ph2[:npt]*radeg, 'g', label='Phase after SMILI2')
ax.grid(1)
ax.set_xlim(0,npt)
ax.set_ylim(-360,360)

ax.set_title('Visibility Phases for ALMA Observations Before and After SMILI2')
ax.set_xlabel('Time (contingent units)')
ax.set_ylabel('Phase (deg)')
degrng = np.arange(-360, 390, 60)
ax.set_yticklabels(degrng)
ax.set_yticks(degrng)

ax.legend()

plt.show()
        
