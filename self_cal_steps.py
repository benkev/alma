#
# self_cal_steps.py
#
# Self-calibration steps for noisy and noiseless observations
#
# Running:
#   First set two string variables (see below):
#   pdir to the project (and the project directory) name;
#   ns = '_mynoise' for the noisy observation, or ns = '' for the noiseless one.
#   Then type at the casa prompt:
# execfile('self_cal_steps.py')
#


import matplotlib.pyplot as plt
import numpy as np
import sys
# from alma_util import workdir

niter = 5000

pdir = 'alma/'
ns = ''
ns = '_mynoise'

#
# 1st iteration
#

print('1st iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10'+ns+'.ms to image "'+
      pdir+'1st_ns.*/" ...')

tclean(vis=pdir+'alma.alma.cycle7.10'+ns+'.ms', imagename=pdir+'1st_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating '+pdir+'alma_phase_ns_1.cal...')

gaincal(vis=pdir+'alma.alma.cycle7.10'+ns+'.ms',
        caltable=pdir+'alma_phase_ns_1.cal',
        solint='30s', calmode='p', gaintype='G', refant='A135')

print('...done.')
print('applycal...')

applycal(vis=pdir+'alma.alma.cycle7.10'+ns+'.ms',
         gaintable=pdir+'alma_phase_ns_1.cal') 

print('...done.')
print('split to '+pdir+'alma.alma.cycle7.10'+ns+'_selfcal_1.ms ...')

split(vis=pdir+'alma.alma.cycle7.10'+ns+'.ms',
      outputvis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_1.ms',
      datacolumn='corrected')  

print('...done. \n')


#
# 2nd iteration
#

print('2nd iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10'+ns+'_selfcal_1.ms to image "'+
      pdir+'2nd_ns.*/"...')

tclean(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_1.ms',
       imagename=pdir+'2nd_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating '+pdir+'alma_phase_ns_2.cal ...')

gaincal(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_1.ms',
        caltable=pdir+'alma_phase_ns_2.cal',
        solint='30s',
        calmode='p', gaintype='G', refant='A135')

print('...done.')
print('applycal...')

applycal(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_1.ms',
         gaintable=pdir+'alma_phase_ns_2.cal') 

print('...done.')
print('split to '+pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms ...')

split(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_1.ms',
      outputvis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 3rd iteration
#

print('3rd iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms to image "'+
      pdir+'3rd_ns.*/"...')

tclean(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms',
       imagename=pdir+'3rd_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')
print('gaincal: creating '+pdir+'alma_phase_ns_3.cal ...')

gaincal(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms',
        caltable=pdir+'alma_phase_ns_3.cal',
        solint='30s',
        calmode='p', gaintype='G', refant='A135')

print('...done.')
print('applycal...')

applycal(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms',
         gaintable=pdir+'alma_phase_ns_3.cal') 

print('...done.')
print('split to '+pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms ...')

split(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_2.ms',
      outputvis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_3.ms',
      datacolumn='corrected')  

print('...done. \n')



#
# 4th iteration
#

print('4th iteration.')
print('tclean '+pdir+'alma.alma.cycle7.10'+ns+'_selfcal_3.ms to image "'+
      pdir+'4th_ns.*/"...')

tclean(vis=pdir+'alma.alma.cycle7.10'+ns+'_selfcal_3.ms',
       imagename=pdir+'4th_ns',
       imsize=[1024,1024],
       cell='0.00032arcsec', interactive=False, savemodel='modelcolumn',
       datacolumn='data', niter=niter) 

print('...done.')

