from plone.browserlayer.utils import registered_layers
from Products.Scrawl.browser.interfaces import IScrawlLayer
from Products.Scrawl.tests.base import ScrawlTestCase
from Products.Scrawl.config import BLOG_ENTRY_NAME

class TestProductUninstallation(ScrawlTestCase):
    """ Ensure we leave no trace.
    """
    def afterSetUp(self):
        self.portal_types = self.portal.portal_types
        qi = self.portal.portal_quickinstaller
        if qi.isProductInstalled('Scrawl'):
            qi.uninstallProducts(products=['Scrawl',])
            
    def test_browser_layer_uninstalled(self):
        self.failIf(IScrawlLayer in registered_layers())
    
    def test_types_restored(self):
        # no more Blog Entry
        self.failIf(BLOG_ENTRY_NAME in self.portal_types.objectIds())

    def test_topic_fti_restored(self):
        # no more blog_view
        self.failIf('blog_view' in self.portal_types.Topic.view_methods)

    def test_portal_factory_restored(self):
        self.failIf('Blog Entry' in self.portal.portal_factory.getFactoryTypes(),
                    '"Blog Entry" still in the portal factory, post uninstall.')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductUninstallation))
    return suite