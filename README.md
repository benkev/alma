# alma
SMILI2 development for ALMA

Tests how correctly SMILI2 loads/saves CASA generated fits files.

RoundSpottyDisk_Betelgeuse.py - Create a sky image in CASA
simulated_obs_alma.py         - simobserve it
simulated_obs_alma_smili.py   - simobserve it after load/save in SMILI2
diff_fits.py                  - differences between fits before and after SMILI2
diff_ms.py                    - differences between visibilities

    ============== !!!!!! EXTREMELY IMPORTANT !!!!! ================

Please copy the Python module alma_util.py to your current CASA version's
site-packages directory.

For CASA release 5.4.0:

$ cp alma_util.py /home/benkev/bin/casa-release-5.4.0-68.el7/lib/python2.7/site-packages/

For CASA 6.1.0:

$ cp alma_util.py /home/benkev/bin/casa-6.1.0-118/lib/py/lib/python3.6/site-packages/

Please find your site-packages from inside your CASA release with the command:

$ find . -name "site-packages"

