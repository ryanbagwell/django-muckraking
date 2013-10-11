Django Muckraking
=================

A collection of various Django utilities. It includes:


Middleware
----------

Spaceless Middleware - muckraking.middleware.SpacelessMiddleware
    Removes spaces and line breaks between html tags. Leaves <script> blocks intact


Legacy URL Redirect Middleware - muckraking.middleware.LegacyURLRedirectMiddleware
    An apache-like approach to redirects.

    Specify your redirects in settings.py like this::

        LEGACY_URL_REDIRECTS = (
            (r'^/about/news-events\.php(.+)?', '/news-events/$1',),
            (r'^/about/(?!index\.php)', '/about/',),
        )


Template Context Processors
---------------------------

Debug Context - muckraking.template.context_processors.debug_context
    Add a :code:`{{ DEBUG }}` variable Django templates. The value is a boolean


Standard Template Tags
----------------------

To use the following tags, add {% load muckraking_tags %} to your template.

Git Head Hash
    Outputs the commit hash of the HEAD commit in a git repo. Useful for cache-busting strings::

    {% git_commit_hash %}



Django CMS Template Tags
------------------------

To use the following tags, add :code:`{% load muckraking_cms_tags %}` to your template.

Get Page URL By Slug
    Allows you to perform reverse lookups on pages by slug::

    {% page_url_by_slug "foobar-page" %}


