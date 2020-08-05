# rxtouchtoggle
Touch toggle for indicator for Xubuntu.

### Running tests
To run all tests:  
`nox`

To run a specific test suite:  
`nox -e lint`

To run a specific test module:  
`nox -e test -- -k test_calc` (To see print statements of passing tests use the `-s` flag)

To try out module:  
`rxtouchtoggle add 1 2`

To install from github:  
`pip3 install --user git+https://github.com/aldencolerain/rxtouchtoggle.git#egg=rxtouchtoggle`

To uninstall:  
`pip3 uninstall rxtouchtoggle`
