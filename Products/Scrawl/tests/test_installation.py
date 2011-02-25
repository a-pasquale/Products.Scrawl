from plone.browserlayer.utils import registered_layers
from Products.Scrawl.browser.interfaces import IScrawlLayer
from Products.Scrawl.tests.base import ScrawlTestCase
from Products.Scrawl.config import BLOG_ENTRY_NAME

class TestProductInstallation(ScrawlTestCase):
    """ Ensure that our product installs properly
    """
    def afterSetUp(self):
        self.portal_types = self.portal.portal_types
        
    def testBrowserLayerInstalled(self):
        self.failUnless(IScrawlLayer in registered_layers())

    def testBlogEntryInstalled(self):
        self.failUnless(BLOG_ENTRY_NAME in self.portal_types.objectIds())

    def testBlogViewAvailable(self):
        self.failUnless('blog_view' in self.portal_types.Topic.view_methods)

    def testBlogEntryViewAvailable(self):
        """If the default view method isn't listed in the available view methods
        Plone 4.0's type settings protests."""
        be = getattr(self.portal_types, BLOG_ENTRY_NAME)
        self.failUnless('blogentry_view' in be.view_methods)
        
    def testBlogEntryDescription(self):
        """Blog Entry shouldn't show (type) description of the 'News Item'."""
        be = getattr(self.portal_types, BLOG_ENTRY_NAME)
        self.assertEquals(be.description, u'A blog entry that will show up in the blog view.')

    def testPortalFactorySetup(self):
        self.failUnless('Blog Entry' in self.portal.portal_factory.getFactoryTypes(),
                        '"Blog Entry" is not available in the portal factory.')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstallation))
    return suite