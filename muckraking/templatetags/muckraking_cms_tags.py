"""Django CMS Template Tags

.. moduleauthor:: Ryan Bagwell <ryan@ryanbagwell.com>


"""
from classytags.arguments import Argument
from classytags.core import Tag, Options
from django import template
from cms.models.titlemodels import Title

register = template.Library()


class PageURLBySlug(Tag):
    """ Looks up a page url by its slug.
        Why doesn't django CMS have this tag built in?
    """
    name = "page_url_by_slug"

    options = Options(
        Argument('page_slug', required=False, default=''),
    )

    def render_tag(self, context, page_slug):


        try:
            return Title.objects.filter(slug=page_slug).exclude(
                title='')[0].page.get_absolute_url()
        except:
            return ''

register.tag(PageURLBySlug)