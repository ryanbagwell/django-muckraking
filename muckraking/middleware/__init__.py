import re
import os
from django.http import HttpResponsePermanentRedirect
from django.utils.html import strip_spaces_between_tags as short
from django.conf import settings


class SpacelessMiddleware(object):
    """ Removes spaces and line breaks
        from templates when DEBUG is False """

    def process_response(self, request, response):

        if not settings.DEBUG and 'text/html' in response['Content-Type']:
            response.content = short(response.content)
        return response



class LegacyURLRedirectMiddleware:

    """ This middleware lets you match a specific url and redirect
        the request to an new url.

        You keep a tuple of url regex pattern/url redirect tuples on your site
        settings.

        For example, in settings.py:

        LEGACY_URL_REDIRECTS = (
            (r'^/about/news-events\.php(.+)?', '/news-events/$1',),
            (r'^/about/(?!index\.php)', '/about/',),
        )

        """

    def process_request(self, request):

        path = request.META['PATH_INFO']

        LEGACY_URL_REDIRECTS = getattr(settings, 'LEGACY_URL_REDIRECTS', None)

        if LEGACY_URL_REDIRECTS is None: return

        for url_pattern, redirect_url in LEGACY_URL_REDIRECTS:
            regex = re.compile(url_pattern)
            matched = regex.match(path)

            if matched:
                print matched.groups()

                for i, group in enumerate(matched.groups(), start=1):
                    print group
                    redirect_url = redirect_url.replace("$%s" % str(i), group)

                return HttpResponsePermanentRedirect(redirect_url)