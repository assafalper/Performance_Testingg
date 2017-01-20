whil-test-automation-framework

## [Whil](https://www.whil.com/) QA: Selenium Test Automation Framework

written in
## Python 3.5 / Selenium 3.0.2 / Behave 1.2.5
Using py.test as default runner


**App package** includes _application.py_ that contains references to all web pages.

**Pages package** contains classes and methods for all web pages.
Note, every page should inherit Page object from _base.py_.

**Tests package** contains test steps, environment and features (scenarios).
To run the tests - run all _.feature_ files in 'tests' folder
- feature files contain test scenarios written in standard English
- test steps define every scenario statement and translate English to Python
- environment file links test steps to App package and defines set of methods to execute _before_ and _after_ every test 
scenario; change base_url to point to prod, qa or localhost.

##### Useful links:
- [BDD and Behave](http://pythonhosted.org/behave/)
- [Selenuim and Python: drivers and installation](https://pypi.python.org/pypi/selenium)
- [Selenium and Python: how to, main classes and methods](http://selenium-python.readthedocs.io/installation.html)

##
###_Happy testing! Behave!_