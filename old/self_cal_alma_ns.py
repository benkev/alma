#
# self_cal_alma_ns.py
#
# Self-calibration steps for noisy observations
#


import matplotlib.pyplot as plt
import numpy as np
import sys
# from alma_util import workdir

niter = 5000

pdir = 'alma/'

#
# 1st iteration
#

print('1st iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10_mynoise.ms to image "'+
      pdir+'1st_ns.*/" ...')

tclean(vis=pdir+'alma.alma.cycle7.10_mynoise.ms', imagename=pdir+'1st_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating '+pdir+'alma_phase_ns_1.cal...')

gaincal(vis=pdir+'alma.alma.cycle7.10_mynoise.ms',
        caltable=pdir+'alma_phase_ns_1.cal',
        solint='30s', calmode='p', gaintype='G', refant='A135')

print('...done.')
print('applycal...')

applycal(vis=pdir+'alma.alma.cycle7.10_mynoise.ms',
         gaintable=pdir+'alma_phase_ns_1.cal') 

print('...done.')
print('split to '+pdir+'alma.alma.cycle7.10_mynoise_selfcal_1.ms ...')

split(vis=pdir+'alma.alma.cycle7.10_mynoise.ms',
      outputvis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_1.ms',
      datacolumn='corrected')  

print('...done. \n')


#
# 2nd iteration
#

print('2nd iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10_mynoise_selfcal_1.ms to image "'+
      pdir+'2nd_ns.*/"...')

tclean(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_1.ms',
       imagename=pdir+'2nd_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating '+pdir+'alma_phase_ns_2.cal ...')

gaincal(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_1.ms',
        caltable=pdir+'alma_phase_ns_2.cal',
        solint='30s',
        calmode='p', gaintype='G', refant='A135')

print('...done.')
print('applycal...')

applycal(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_1.ms',
         gaintable=pdir+'alma_phase_ns_2.cal') 

print('...done.')
print('split to '+pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms ...')

split(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_1.ms',
      outputvis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 3rd iteration
#

print('3rd iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms to image "'+
      pdir+'3rd_ns.*/"...')

tclean(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms',
       imagename=pdir+'3rd_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating '+pdir+'alma_phase_ns_3.cal ...')

gaincal(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms',
        caltable=pdir+'alma_phase_ns_3.cal',
        solint='30s',
        calmode='p', gaintype='G', refant='A135')

print('...done.')
print('applycal...')

applycal(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms',
         gaintable=pdir+'alma_phase_ns_3.cal') 

print('...done.')
print('split to '+pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms ...')

split(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_2.ms',
      outputvis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_3.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 4th iteration
#

print('4th iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10_mynoise_selfcal_3.ms to image "'+
      pdir+'4th_ns.*/"...')

tclean(vis=pdir+'alma.alma.cycle7.10_mynoise_selfcal_3.ms',
       imagename=pdir+'4th_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')

