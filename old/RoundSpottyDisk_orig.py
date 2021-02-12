# Make a circular spotted disk

# In CASA

direction = "J2000 02h00m00.0s -02d00m00.0s"
direction2= "J2000 02h00m00.00013s -02d00m00.010s"
direction3= "J2000 01h59m59.9992s -02d00m00.015s"
direction4 = "J2000 02h00m00.0002s -01d59m59.982s"
direction5 = "J2000 02h00m00.0023s -01d59m59.998s"

cl.done()

# Make the size equivalent to 80 mas, the size of Betelgeuse found by Lim et al. at 46 GHz.
cl.addcomponent(dir=direction, flux=28.0e-3, fluxunit='Jy', freq='46.1GHz', shape="disk", 
                majoraxis="0.0013arcmin", minoraxis='0.0013arcmin', positionangle='0.0deg')

# Make some spots

# bright region: offset by -10mas in DEC, 20 mas in RA
#cl.addcomponent(dir=direction2, flux=0.01e-3, fluxunit='Jy', freq='46.1GHz', shape="Gaussian", 
#                majoraxis="0.000013arcmin", minoraxis='0.000013arcmin', positionangle='0.0deg')

# dark region; offset by -15mas in DEC, -12 mas in RA
cl.addcomponent(dir=direction3, flux=-11.2e-4, fluxunit='Jy', freq='46.1GHz', shape="Gaussian", 
                majoraxis="0.0004arcmin", minoraxis='0.0004arcmin', positionangle='0.0deg')

# dark region; offset by +30 mas in RA, +18mas in DEC
cl.addcomponent(dir=direction4, flux=-2.24e-4, fluxunit='Jy', freq='46.1GHz', shape="Gaussian", 
                majoraxis="0.0003arcmin", minoraxis='0.0003arcmin', positionangle='0.0deg')

# bright region: offset by +2mas DEC, +35mas in RA
cl.addcomponent(dir=direction5, flux=5.6e-5, fluxunit='Jy', freq='46.1GHz', shape="Gaussian", 
                majoraxis="0.00006arcmin", minoraxis='0.00006arcmin', positionangle='0.0deg')
#
#ia.fromshape("RoundSpottyDisk_orig.im",[8196,8196,1,1],overwrite=True)
ia.fromshape("RoundSpottyDisk_orig.im",[4096,4096,1,1],overwrite=True)
cs=ia.coordsys()
cs.setunits(['rad','rad','','Hz'])
cell_rad=qa.convert(qa.quantity("0.00008arcsec"),"rad")['value']
cs.setincrement([-cell_rad,cell_rad],'direction')
cs.setreferencevalue([qa.convert("02h",'rad')['value'],qa.convert("-02deg",'rad')['value']],type="direction")
cs.setreferencevalue("46.1GHz",'spectral')
cs.setincrement('1GHz','spectral')
ia.setcoordsys(cs.torecord())
ia.setbrightnessunit("Jy/pixel")
ia.modify(cl.torecord(),subtract=False)


exportfits(imagename='RoundSpottyDisk_orig.im',fitsimage='RoundSpottyDisk_orig.fits',overwrite=True)
