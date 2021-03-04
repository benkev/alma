#
# self_cal_smili.py
#
# Self-calibration steps
#

import matplotlib.pyplot as plt
import numpy as np
# from alma_util import workdir

niter = 5000

#
# 1st iteration
#

print('1st iteration.')
print('tclean alma_smili.alma.cycle7.10.ms to image "1st.*/" ...')

tclean(vis='alma_smili.alma.cycle7.10.ms', imagename='1st', imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating smili_phase_1.cal...')

gaincal(vis='alma_smili.alma.cycle7.10.ms', caltable="smili_phase_1.cal",
        solint="30s", calmode="p", gaintype="G", refant='A135')

print('...done.')
print('applycal...')

applycal(vis='alma_smili.alma.cycle7.10.ms', gaintable='smili_phase_1.cal') 

print('...done.')
print('split to alma_smili.alma.cycle7.10_selfcal_1.ms ...')

split(vis='alma_smili.alma.cycle7.10.ms',
      outputvis='alma_smili.alma.cycle7.10_selfcal_1.ms',
      datacolumn='corrected')  

print('...done. \n')


#
# 2nd iteration
#

print('2nd iteration.')
print('tclean alma_smili.alma.cycle7.10_selfcal_1.ms to image "2nd.*/"...')

tclean(vis='alma_smili.alma.cycle7.10_selfcal_1.ms', imagename='2nd',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating smili_phase_2.cal ...')

gaincal(vis='alma_smili.alma.cycle7.10_selfcal_1.ms',
        caltable="smili_phase_2.cal",
        solint="30s",
        calmode="p", gaintype="G", refant='A135')

print('...done.')
print('applycal...')

applycal(vis='alma_smili.alma.cycle7.10_selfcal_1.ms',
         gaintable='smili_phase_2.cal') 

print('...done.')
print('split to alma_smili.alma.cycle7.10_selfcal_2.ms ...')

split(vis='alma_smili.alma.cycle7.10_selfcal_1.ms',
      outputvis='alma_smili.alma.cycle7.10_selfcal_2.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 3rd iteration
#

print('3rd iteration.')
print('tclean alma_smili.alma.cycle7.10_selfcal_2.ms to image "3rd.*/"...')

tclean(vis='alma_smili.alma.cycle7.10_selfcal_2.ms', imagename='3rd',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating smili_phase_3.cal ...')

gaincal(vis='alma_smili.alma.cycle7.10_selfcal_2.ms',
        caltable="smili_phase_3.cal",
        solint="30s",
        calmode="p", gaintype="G", refant='A135')

print('...done.')
print('applycal...')

applycal(vis='alma_smili.alma.cycle7.10_selfcal_2.ms',
         gaintable='smili_phase_3.cal') 

print('...done.')
print('split to alma_smili.alma.cycle7.10_selfcal_2.ms ...')

split(vis='alma_smili.alma.cycle7.10_selfcal_2.ms',
      outputvis='alma_smili.alma.cycle7.10_selfcal_3.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 4th iteration
#

print('4th iteration.')
print('tclean alma_smili.alma.cycle7.10_selfcal_3.ms to image "4th.*/"...')

tclean(vis='alma_smili.alma.cycle7.10_selfcal_3.ms', imagename='4th',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')

