from Products.CMFCore.DirectoryView import registerDirectory
from Products.Scrawl.config import GLOBALS

registerDirectory('skins', GLOBALS)

# Parts of the installation process depend on the version of Plone.
# This release supports Plone 2.5 and Plone 3.* 
try:
    from Products.CMFPlone.migrations import v3_0
except ImportError:
    HAS_PLONE30 = False
else:
    HAS_PLONE30 = True
    
# This release also supports Plone 4.0; for now we handle Plone 4.* 
# similar to Plone 3.*
try:
    from Products.CMFPlone.factory import _IMREALLYPLONE4
except ImportError:
    pass
else:
    HAS_PLONE30 = True
    

def initialize(context):
    pass