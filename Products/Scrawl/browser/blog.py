from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from cloudspring.sfmembers import membership
import re

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

    def getHomeUrl(self, id):
        url = membership.getHomeUrl(self.context, id) 
        return url

    def isCreator(self, item_creator):
        #item_creator = self.context.Creator()
        mt = getToolByName(self.context, 'portal_membership')
        member = mt.getAuthenticatedMember()
        if member.getUserName() == item_creator:
            return True

    def inHomeFolder(self, id):
        home_url = self.getHomeUrl(id)
        if home_url:
            current_path = self.request.URL
            if re.search(home_url, current_path):
                return True
