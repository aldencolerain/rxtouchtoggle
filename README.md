# rxtouchtoggle
Touch toggle for indicator for Xubuntu.

### Installation
To install locally in editable mode (this has to be manually uninstalled):  
`pip3 install --user -e .`

To install from github:  
`pip3 install --user git+https://github.com/aldencolerain/rxtouchtoggle.git#egg=rxtouchtoggle`

To uninstall:  
`pip3 uninstall rxtouchtoggle`


### Running on startup in Xubuntu:
Click on *Whisker Menu* and open *Session and Startup*.  Then select the *Application Autostart*
tab and create a new entry that runs `rxtouchtoggle start` on startup.

### Running tests
To run all tests:  
`nox`

To run a specific test suite:  
`nox -e lint`

To run a specific test module:  
`nox -e test -- -k test_calc` (To see print statements of passing tests use the `-s` flag)
