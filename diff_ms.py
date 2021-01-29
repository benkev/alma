import matplotlib.pyplot as plt
import numpy as np

msn1 = 'alma/alma.alma.cycle7.10.ms'
msn2 = 'alma_smili/alma_smili.alma.cycle7.10.ms/'

cols = ['antenna1', 'antenna2', 'u', 'v', 'w', 'data',
                         'flag', 'flag_row']


#met = ms.metadata()

# spw = 0  # Spectral window
# field = 0
# ipol = 0
# times = md.timesforfield(field) # Get all the times for MS
# times = np.array(times)
# ymds = []     # List of string representations of times
# for tim in times:
#     qtim = qa.quantity(tim, 's') # {'unit':'s','value': 4953324816.75}
#     ymd = qa.time(qtim, form='ymd', prec=8) # 8 means .../12:34:56.78
#     ymds.append(ymd[0])


ms.open(msn1, nomodify=True)

ms.selectinit(datadescid=0)      # Reset all previous selections

rec = ms.getdata(cols)
dat1 = np.squeeze(rec['data'])

ms.close()

ms.open(msn2, nomodify=True)

ms.selectinit(datadescid=0)      # Reset all previous selections

rec = ms.getdata(cols)
dat2 = np.squeeze(rec['data'])

ms.close()

dif = abs(dat2 - dat1)
dif = dif[0]

absd1 = np.abs(dat1)[0]
absd2 = np.abs(dat2)[0]

if np.any(abs(absd1 - absd2) == 0.):
    print('Data in', msn, 'and', msn2, 'are identical.')
else:
    print('Data in', msn1, 'and', msn2, 'are different.')

ph = np.angle(dat2 - dat1)[0]

plt.figure(); plt.plot(ph); plt.grid(1) 





        
