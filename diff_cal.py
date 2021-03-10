#
# diff_cal.py
#
# Call parameters:
#
# $ python diff_cal.py  caltable1.cal/  caltable2.cal/ measurement_set1.ms/
#

import matplotlib.pyplot as plt
import numpy as np
import casacore.tables.table as castb
#import casacore.tables.tablecolumn as castc
import sys

scal1 = sys.argv[1]  # First calibration table directory name
scal2 = sys.argv[2]  # Second calibration table directory name
sms1 =  sys.argv[3]  # First MS table directory name

cal1 = castb(scal1)
cal2 = castb(scal2)

ncal1 = len(cal1)
ncal2 = len(cal2)
if ncal1 != ncal2:
    raise SystemExit('The CASA tables have different sizes, %d and %d' %
                     (ncal1, ncal2))
ncal = ncal1

#
# Get antenna names from the ANTENNA subtable
#
ansubt1 = castb(sms1 + '/ANTENNA/')
aname = ansubt1.getcol('NAME')      # Antenna names as list
aname = np.array(aname)

ant1 = np.zeros(ncal, dtype=int)
ant2 = np.zeros(ncal, dtype=int)
dat1 = np.zeros(ncal, dtype=np.complex64)
dat2 = np.zeros(ncal, dtype=np.complex64)
ixant = np.zeros(ncal, dtype=int)        # Antenna indices into 

for ix in range(ncal):
    ant1[ix] = cal1[ix]['ANTENNA1']
    ant2[ix] = cal1[ix]['ANTENNA1']
    dat1[ix] = cal1[ix]['CPARAM'][0,0]
    dat2[ix] = cal2[ix]['CPARAM'][0,0]

mag1 = np.abs(dat1)
mag2 = np.abs(dat2)
pha1 = np.degrees(np.angle(dat1))
pha2 = np.degrees(np.angle(dat2))

#
# Differences in magnitude and phase: dmag and dpha
#
#dmag = mag2 - mag1
dpha = pha2 - pha1

nant = ant1.max() + 1  # Number of antennae
n_per_ant = ncal//nant # Number of records per antenna

#
# Differences in magnitude and phase per antenns: damag and dapha
#
# damag = np.zeros((nant,n_per_ant), dtype=np.float32)
dapha = np.zeros((nant,n_per_ant), dtype=np.float32)

for ia in range(nant):
    #damag[ia,:] = dmag[np.where(ant1 == ia)]
    dapha[ia,:] = dpha[np.where(ant1 == ia)]
    
# plt.figure();
# for ia in range(nant):
#     plt.plot(dapha[ia,:]);
#     plt.plot(dapha[ia,:], '.');
# plt.grid(1)  

mean_dpha = np.mean(dpha)
std_dpha =  np.std(dpha)
plt.figure(); plt.hist(dpha, 50); plt.grid(1)
plt.title('Phase Difference Between Calibration Tables')
plt.text(0.75, 132, 'Mean: %6.3f' % mean_dpha)
plt.text(0.75, 122, 'STD:  %6.3f' % std_dpha)
plt.plot([mean_dpha, mean_dpha], [0,160], 'r--', lw=1.5)
plt.plot([mean_dpha-std_dpha, mean_dpha-std_dpha], [0,80], 'k--', lw=1.5)
plt.plot([mean_dpha+std_dpha, mean_dpha+std_dpha], [0,80], 'k--', lw=1.5)


#
# Means and standard deviations of the differences between calibration tables
# per each individual antenna 
#
mean_dapha = np.mean(dapha, axis=1)
std_dapha = np.std(dapha, axis=1)
ant_rng = np.arange(nant)
zlev = np.zeros(nant)

#
# Plot means and standard deviations
#
# plt.figure()
# plt.plot(ant_rng, zlev, 'k')
# plt.plot(ant_rng, mean_dapha, 'bo', label='Mean')
# plt.plot(ant_rng, std_dapha,  'go', label='STD')
# plt.grid(1)
# plt.legend()
# plt.title('Means and STDs of CalTables Phase Diffs per Antenna')
# plt.xlabel('Antenna #')

#
# Plot means and standard deviations in descending order of the STDs 
#
ixstd = np.argsort(std_dapha)[::-1]  # Index if STDs in descending order

fig = plt.figure(figsize=(12,6))
ax = fig.add_axes( [.05, .13, .92, .80 ] ) 
plt.plot(ant_rng, zlev, 'k')
plt.plot(ant_rng, mean_dapha[ixstd], 'bo', label='Mean')
plt.plot(ant_rng, std_dapha[ixstd],  'go', label='STD')
plt.grid(1)
plt.legend()
plt.title('Means and STDs of CalTables Phase Diffs per Antenna')
plt.xlabel('Antenna Name')
plt.xticks(ant_rng, aname[ixstd], rotation=45)
plt.ylim(-0.2, 0.6)
for ia in ant_rng: plt.text(float(ia)-0.35, -0.19, str(ixstd[ia]))


#
# Print antenna list in the descending order of STDs
#
for ia in ixstd:             # range(nant):
    print('Ant: %2d ("%s"), Mean: %6.3f, STD: %6.3f' %
          (ia, aname[ia], mean_dapha[ia], std_dapha[ia]))
    


plt.show()




