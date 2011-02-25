Description
===========

Scrawl is a dirt-simple blog product for Plone.  It copies the News Item
content type to create a Blog Entry (with a slightly tweaked view template)
and adds an alternative view to Collections (blog_view).  Note that blog_view
shows either the description of each contained blog entry (if it exists) or the
entire body.  It's up to the user to limit those results in an intelligent
way so that page loads doesn't take too long.

Scrawl works in Plone 3.x and 4.0.

Installation
============

Installing using buildout
-------------------------

Simply add Products.Scrawl to your eggs list and rerun buildout.

Add Scrawl to your Plone site
-----------------------------

Go to Site Setup page in Plone and click on Add-ons.


Migration
=========

There is a basic migrator available for Quills -> Scrawl.  Read the docstring
in Products.Scrawl.Extensions.migrate_entries for more details.  YMMV.


Credits
=======

Development by Groundwire_ (formlery ONE/Northwest) <jonb@groundwire.org>.

.. _Groundwire: http://groundwire.org/

Thanks to FamFamFam for the blog entry icon, which is part of the Silk_ set.

.. _Silk: http://www.famfamfam.com/lab/icons/silk/
