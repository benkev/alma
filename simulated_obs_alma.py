#
# simulated_obs_alma.py
#
# Use to generate a simulated ALMA image of the data set  
# RoundSpottyDisk1.fits. Uses 2-hour continuous integrations.
# Noise assumes 10GHz BW, dual pol.
#
import os
from alma_util import workdir

#
# Make this script running universally on our several machines.
#
basedir = workdir() + 'ALMA/'


projdir = 'alma_orig' 
projname = 'alma' 
skymodeln = basedir + 'RoundSpottyDisk.fits'

simobserve(project=projname, skymodel=skymodeln, 
       incell         = '0.00008arcsec', incenter='200GHz', inwidth='1GHz',
       setpointings   = False ,
       ptgfile        = basedir + 'Betelgeusedirection.txt',
       integration    = '300s',
       obsmode        = 'int',
       antennalist    = basedir + 'alma.cycle7.10.cfg',
       hourangle      =  'transit',
       totaltime      = '7200s',
       outframe       = 'LSRK',
       thermalnoise   = '',
       verbose=False)

modelname=projname + '/' + projname + '.alma.cycle7.10.ms'

noisymodelname=projname + '/' + projname + '.alma.cycle7.10_mynoise.ms'

os.system('cp -r ' + modelname + ' ' + noisymodelname) 

sm.openfromms(noisymodelname)
sm.setnoise(mode='simplenoise', simplenoise='0.0001755Jy')
print('Adding noise...' )
sm.corrupt()
sm.done()

fitsout=projname + '/' + projname + '.alma.cycle7.10_mynoise.uvfits'

exportuvfits(vis=noisymodelname,fitsfile=fitsout,
              datacolumn='data', field='',spw='',
              antenna='',timerange='',writesyscal=False,
              multisource=False, combinespw=True,
              writestation=False,overwrite=False)

os.system('mv ' + projname + '/ ' + projdir + '/')
print('mv ' + projname + '/ ' + projdir + '/')

