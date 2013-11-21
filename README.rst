Django Muckraking
=================

A collection of various Django utilities. It includes:


Middleware
----------

:code:`muckraking.middleware.SpacelessMiddleware`
    Removes spaces and line breaks between html tags. Leaves <script> blocks intact


:code:`muckraking.middleware.LegacyURLRedirectMiddleware`
    An apache-like approach to redirects.

    Specify your redirects in settings.py like this::

        LEGACY_URL_REDIRECTS = (
            (r'^/about/news-events\.php(.+)?', '/news-events/$1',),
            (r'^/about/(?!index\.php)', '/about/',),
        )


Template Context Processors
---------------------------

:code:`muckraking.template.context_processors.debug_context`
    Add a :code:`{{ DEBUG }}` variable Django templates. The value is a boolean


Standard Template Tags
----------------------

To use the following tags, add :code:`{% load muckraking_tags %}` to your template.

:code:`{% git_commit_hash %}`
    Outputs the commit hash of the HEAD commit in a git repo. Useful for cache-busting strings


Django CMS Template Tags
------------------------

To use the following tags, add :code:`{% load muckraking_cms_tags %}` to your template.

:code:`{% page_url_by_slug "foobar-page" %}`
    Allows you to perform reverse lookups on pages by slug::


Management Commands
-------------------

import_redirects
    Allows you to import a csv file of redirect urls into the redicet app::

    ./manage.py import_redirects ~/path/to/redirects.csv




