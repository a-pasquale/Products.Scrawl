from Testing import ZopeTestCase as ztc
from Products.CMFPlone.tests import PloneTestCase
ztc.installProduct('Scrawl')
PloneTestCase.setupPloneSite(products=['Scrawl',])

class ScrawlTestCase(PloneTestCase.PloneTestCase):
    """Base class for integration tests.
    """