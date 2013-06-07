from django.conf import settings


def debug_context(request):

    """ Adds the DEBUG setting as a
        template variable """

    return {
        'DEBUG': settings.DEBUG,
    }
