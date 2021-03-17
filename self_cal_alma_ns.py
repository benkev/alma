#
# self_cal_alma_ns.py
#
# Self-calibration steps for noisy observations
#

import matplotlib.pyplot as plt
import numpy as np
# from alma_util import workdir

niter = 5000

#
# 1st iteration
#

print('1st iteration.')
print('tclean alma.alma.cycle7.10_mynoise.ms to image "1st_ns.*/" ...')

tclean(vis='alma.alma.cycle7.10_mynoise.ms', imagename='1st_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating alma_phase_ns_1.cal...')

gaincal(vis='alma.alma.cycle7.10_mynoise.ms', caltable="alma_phase_ns_1.cal",
        solint="30s", calmode="p", gaintype="G", refant='A135')

print('...done.')
print('applycal...')

applycal(vis='alma.alma.cycle7.10_mynoise.ms', gaintable='alma_phase_ns_1.cal') 

print('...done.')
print('split to alma.alma.cycle7.10_mynoise_selfcal_1.ms ...')

split(vis='alma.alma.cycle7.10_mynoise.ms',
      outputvis='alma.alma.cycle7.10_mynoise_selfcal_1.ms',
      datacolumn='corrected')  

print('...done. \n')


#
# 2nd iteration
#

print('2nd iteration.')
print('tclean alma.alma.cycle7.10_mynoise_selfcal_1.ms to image "2nd_ns.*/"...')

tclean(vis='alma.alma.cycle7.10_mynoise_selfcal_1.ms', imagename='2nd_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating alma_phase_ns_2.cal ...')

gaincal(vis='alma.alma.cycle7.10_mynoise_selfcal_1.ms',
        caltable="alma_phase_ns_2.cal",
        solint="30s",
        calmode="p", gaintype="G", refant='A135')

print('...done.')
print('applycal...')

applycal(vis='alma.alma.cycle7.10_mynoise_selfcal_1.ms',
         gaintable='alma_phase_ns_2.cal') 

print('...done.')
print('split to alma.alma.cycle7.10_mynoise_selfcal_2.ms ...')

split(vis='alma.alma.cycle7.10_mynoise_selfcal_1.ms',
      outputvis='alma.alma.cycle7.10_mynoise_selfcal_2.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 3rd iteration
#

print('3rd iteration.')
print('tclean alma.alma.cycle7.10_mynoise_selfcal_2.ms to image "3rd_ns.*/"...')

tclean(vis='alma.alma.cycle7.10_mynoise_selfcal_2.ms', imagename='3rd_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating alma_phase_ns_3.cal ...')

gaincal(vis='alma.alma.cycle7.10_mynoise_selfcal_2.ms',
        caltable="alma_phase_ns_3.cal",
        solint="30s",
        calmode="p", gaintype="G", refant='A135')

print('...done.')
print('applycal...')

applycal(vis='alma.alma.cycle7.10_mynoise_selfcal_2.ms',
         gaintable='alma_phase_ns_3.cal') 

print('...done.')
print('split to alma.alma.cycle7.10_mynoise_selfcal_2.ms ...')

split(vis='alma.alma.cycle7.10_mynoise_selfcal_2.ms',
      outputvis='alma.alma.cycle7.10_mynoise_selfcal_3.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 4th iteration
#

print('4th iteration.')
print('tclean alma.alma.cycle7.10_mynoise_selfcal_3.ms to image "4th_ns.*/"...')

tclean(vis='alma.alma.cycle7.10_mynoise_selfcal_3.ms', imagename='4th_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')

