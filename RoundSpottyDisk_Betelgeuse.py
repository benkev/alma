#
# Make a circular spotted disk at the Betelgeuse sky coordinates in CASA,
# the size equivalent to 80 mas, the size of Betelgeuse found by
# Lim et al. at 46 GHz.
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


bname = homedir + 'ALMA/RoundSpottyDisk'

#
# Betelgeuse
#
ra =  '05h55m10.080s'
dec = '07d24m25.200s'

dir  = 'J2000 05h55m10.0800s 07d24m25.200s'  
dir1 = 'J2000 05h55m10.0792s 07d24m25.185s'  # -12 mas in RA, -15 mas in DEC
dir2 = 'J2000 05h55m10.0802s 07d24m25.218s'  #  +3 mas in RA, +18 mas in DEC
dir3 = 'J2000 05h55m10.0823s 07d24m25.202s'  # +35 mas in RA,  +2 mas in DEC

cl.done()

# Make the size equivalent to 80 mas, the size of Betelgeuse found by
# Lim et al. at 46 GHz.
cl.addcomponent(dir=dir, flux=28.0e-3, fluxunit='Jy',
                freq='46.1GHz', shape="disk",
                majoraxis="0.0013arcmin", minoraxis='0.0013arcmin',
                positionangle='0.0deg')

# Make some spots

# dark region; offset by -12mas in RA, -15mas in DEC
cl.addcomponent(dir=dir1, flux=-11.2e-4, fluxunit='Jy',
                freq='46.1GHz', shape="Gaussian", 
                majoraxis="0.0004arcmin", minoraxis='0.0004arcmin',
                positionangle='0.0deg')

# dark region; offset by +3mas in RA, +18mas in DEC
cl.addcomponent(dir=dir2, flux=-2.24e-4, fluxunit='Jy',
                freq='46.1GHz', shape="Gaussian", 
                majoraxis="0.0003arcmin", minoraxis='0.0003arcmin',
                positionangle='0.0deg')

# bright region: offset by +35mas in RA,  +2mas DEC,
cl.addcomponent(dir=dir3, flux=5.6e-5, fluxunit='Jy',
                freq='46.1GHz', shape="Gaussian", 
                majoraxis="0.00006arcmin", minoraxis='0.00006arcmin',
                positionangle='0.0deg')

ia.fromshape(bname + ".im", [4096,4096,1,1], overwrite=True)

cs=ia.coordsys()
cs.setunits(['rad','rad','','Hz'])
cell_rad=qa.convert(qa.quantity("0.00008arcsec"),"rad")['value']
cs.setincrement([-cell_rad,cell_rad],'direction')
cs.setreferencevalue([qa.convert("05h55m10.0800s",'rad')['value'],
                      qa.convert("07d24m25.200s",'rad')['value']],
                     type="direction")
cs.setreferencevalue("46.1GHz",'spectral')
cs.setincrement('1GHz','spectral')
ia.setcoordsys(cs.torecord())
ia.setbrightnessunit("Jy/pixel")
ia.modify(cl.torecord(),subtract=False)


exportfits(imagename=bname + '.im', fitsimage=bname + '.fits',
           overwrite=True)

