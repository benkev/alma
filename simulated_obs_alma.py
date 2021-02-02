#
# Use to generate a simulated ALMA image of the data set  
# RoundSpottyDisk1.fits. Uses 2-hour continuous integrations.
# Noise assumes 10GHz BW, dual pol.
#
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

projectn = 'alma' 
skymodeln = basedir + 'RoundSpottyDisk.fits'

simobserve(project=projectn, skymodel=skymodeln, 
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

modelname=projectn + '/' + projectn + '.alma.cycle7.10.ms'

noisymodelname=projectn + '/' + projectn + '.alma.cycle7.10_mynoise.ms'

os.system('cp -r ' + modelname + ' ' + noisymodelname) 

sm.openfromms(noisymodelname)
sm.setnoise(mode='simplenoise', simplenoise='0.0001755Jy')
print('Adding noise...' )
sm.corrupt()
sm.done()

fitsout=projectn + '/' + projectn + '.alma.cycle7.10_mynoise.uvfits'

exportuvfits(vis=noisymodelname,fitsfile=fitsout,
              datacolumn='data', field='',spw='',
              antenna='',timerange='',writesyscal=False,
              multisource=False, combinespw=True,
              writestation=False,overwrite=False)


