from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
try:
    from plone.app.discussion.interfaces import IConversation, IDiscussionLayer
    HAS_PAD = True
except ImportError:
    HAS_PAD = False
    
class BlogView(BrowserView):
    """
    Listing of blog items. Based on BlogView from collective.blog.view.
    """
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.portal_discussion = getToolByName(self.context, 'portal_discussion')
        
    def comment_count(self, obj):
        """
        Returns the number of comments for the given object or False if
        comments are disabled.
        """
        
        if HAS_PAD:
            if IDiscussionLayer.providedBy(self.request):
                conversation = IConversation(obj)
                return conversation.enabled() and len(conversation)
        if self.portal_discussion.isDiscussionAllowedFor(obj):
            discussion = self.portal_discussion.getDiscussionFor(obj)
            return discussion.replyCount(obj)
        return False
        
    def content_filter(self):
        """
        Returns a dictionary of criteria to pass to the query method.
        """
        
        if 'Subject' in self.request.form:
            return {'Subject': self.request.form.get('Subject')}
        return {}

    def getHome(self, id=None):
        if id is None:
            # If no id is passed, get the currently
            # authenticated user.
            mt = getToolByName(self.context, 'portal_membership')
            member = mt.getAuthenticatedMember()
            id = member.getUserName()
        # Find the users home folder in the catalog.
        catalog = getToolByName(self.context, 'portal_catalog')
        results = catalog.searchResults(
                    {'portal_type': 'Folder', 
                     'path': {'query': '/Plone/members', 
                              'depth': 2},
                     'id': id})
        for brain in results:
            return brain

    def getBlog(self, id=None):
        portal_url = getToolByName(self.context, "portal_url")
        blog = portal_url.unrestrictedTraverse(getHome(context, id).getPath())
        return blog

    def getHomeUrl(self, id=None):
        home = self.getHome(id)
        import logging
        logger = logging.getLogger("blogview")
        logger.info("home: %s" % home.getURL())
        if home is not None:
            return home.getURL()
