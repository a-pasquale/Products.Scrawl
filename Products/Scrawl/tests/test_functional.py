"""
    Scrawl functional doctests (based on the on from CMFPlone).  This module collects all *.txt
    files in the tests directory and runs them.

    See also ``test_doctests.py``.

"""

import os
import glob
from zope.testing import doctest
import unittest
from App.Common import package_home
from Testing.ZopeTestCase import FunctionalDocFileSuite as Suite
from Products.Scrawl.tests.base import ScrawlFunctionalTestCase
from Products.Scrawl.config import GLOBALS



OPTIONFLAGS = (
    #doctest.REPORT_ONLY_FIRST_FAILURE |
    doctest.ELLIPSIS |
    doctest.NORMALIZE_WHITESPACE
)

def list_doctests():
    home = package_home(GLOBALS)
    return [filename for filename in
          glob.glob(os.path.sep.join([home, 'tests/*.txt']))]


def test_suite():
    filenames = list_doctests()

    suites = [Suite(os.path.basename(filename),
               optionflags=OPTIONFLAGS,
               package='Products.Scrawl.tests',
               test_class=ScrawlFunctionalTestCase
               )
              for filename in filenames]

    return unittest.TestSuite(suites)



















