from Testing import ZopeTestCase as ztc
ztc.installProduct('Scrawl')

from Products.PloneTestCase import PloneTestCase
PloneTestCase.setupPloneSite(products=['Scrawl',])

class ScrawlTestCase(PloneTestCase.PloneTestCase):
    """Base class for integration tests.
    """
    
class ScrawlFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """Base class for functional tests.
    """
    