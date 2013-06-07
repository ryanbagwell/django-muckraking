from django.utils.html import strip_spaces_between_tags as short
from django.conf import settings


class SpacelessMiddleware(object):
    """ Removes spaces and line breaks
        from templates when DEBUG is False """

    def process_response(self, request, response):

        if not settings.DEBUG and 'text/html' in response['Content-Type']:
            response.content = short(response.content)
        return response