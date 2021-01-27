# Use to generate a simulated ngVLA image of the data set  
# RoundSpottyDisk.fits. Uses 2-hour continuous integrations.
# Noise assumes 10GHz BW, dual pol.
# Within CASA, execute with:
# execfile('frames_script2.py')



    projectn= 'CFRAME00' 
    skymodeln='/data/home/lmatthew/sparselab/ngVLA/RoundSpottyDisk.fits'
    simobserve(project=projectn, skymodel=skymodeln, 
           incell         = '0.00005arcsec', incenter='46.1GHz', inwidth='1GHz',
           setpointings        =      False ,
           ptgfile        = '/data/home/lmatthew/Betelgeusedirection.txt',
           integration    =     '300s',
           obsmode             =      'int',
           antennalist    = '/data/home/lmatthew/ngVLA/Study2019/CASA/ngVLA-config-revC_forweb/ngvla-main-revC.cfg',
           hourangle      =  'transit',
           totaltime='7200s', outframe            =     'LSRK',
           thermalnoise        =         '',verbose             =      False)
    modelname=projectn + '/' + projectn + '.ngvla-main-revC.ms'
    noisymodelname=projectn + '/' + projectn + '.ngvla-main-revC_mynoise.ms'
    os.system('cp -r ' + modelname + ' ' + noisymodelname) 
    sm.openfromms(noisymodelname)
    sm.setnoise(mode='simplenoise', simplenoise='0.0001755Jy')
    print 'Adding noise...' 
    sm.corrupt()
    sm.done()
    fitsout=projectn + '/' + projectn + '.ngvla-main-revC_mynoise.uvfits'
    exportuvfits(vis=noisymodelname,fitsfile=fitsout,
                  datacolumn='data', field='',spw='',
                  antenna='',timerange='',writesyscal=False,
                  multisource=False, combinespw=True,
                  writestation=False,overwrite=False)


