"""General-use emplate tags

.. moduleauthor:: Ryan Bagwell <ryan@ryanbagwell.com>


"""
from classytags.arguments import Argument
from classytags.core import Tag, Options
from django.conf import settings
from git import Repo
import os
from django import template
import hashlib

register = template.Library()


class EnqueueScript(Tag):
    """A WordPress-inspired template tag that allows you to add javascript to the scripts queue

    Args:
        name (str): a name for your script (i.e. jquery)
        src (str): the script's src attribute
        deps (str): a comma-seperated list of names of scripts that the script depends on
        version (int): the script version.

    """

    name = 'enqueue_script'

    options = Options(
        Argument('name', required=True),
        Argument('src', required=True),
        Argument('deps', required=False, default=''),
        Argument('version', required=False, default=1),
    )

    def render_tag(self, context, name, src, deps, version):
        queue = context.get('queue', {})
        queue[name]= DataScript(name, src, deps, version)
        context['queue'] = queue
        return ""

register.tag(EnqueueScript)



class RenderScripts(Tag):
    """A template tag that renders the scripts added to the script queue with {% enqueue_script %}

    """

    name = 'render_scripts'
    order = []

    def render_tag(self, context):
        self.queue = context.get('queue', {})

        for name, script in self.queue.iteritems():

            for dep in script.deps:

                if dep == '': continue

                if dep not in self.order:
                    self.order.append(dep)

                elif name in self.order:
                    popped = self.order.pop(self.order.index(name))
                    self.order.insert(self.order.index(dep) + 1, popped)

                else:
                    self.order.insert(self.order.index(dep) + 1, script.name)

            if name not in self.order:
                self.order.append(script.name)

        return '\n'.join([ self.queue[script].__unicode__() for script in self.order])

register.tag(RenderScripts)



class VersionHashTag(Tag):
    """ A template tag that outputs a unique hash
        for version purposes. First, it tries to obtain the
        latest git commit hash. If unsuccessful, it provides a hash
        of the last time the settings file was accessed.

        Useful for cache-busting url params """

    name = 'version_hash'

    def render_tag(self, context):

        git_hash = self.get_git_hash()

        if git_hash is '000000':
            return self.get_atime_hash()
        else:
            return git_hash

    def get_atime_hash(self):

        try:
            settings_file = __import__(settings.SETTINGS_MODULE).__file__
            a_time = os.stat(settings_file).st_atime
            h = hashlib.md5()
            h.update(str(a_time))
            return h.hexdigest()
        except:
            return '000000'

    def get_git_hash(self):

        try:
            repo = Repo(os.path.dirname(__import__(settings.ROOT_URLCONF).__file__))
            return repo.heads[0].commit.hexsha
        except:
            return '000000'

register.tag(VersionHashTag)


class GitHeadHash(VersionHashTag):
    """ A template tag that outputs the HEAD commit hash
        of the current branch, if it exists.

        Useful for cache-busting url params """


    name = 'git_commit_hash'

    def render_tag(self, context):

        return self.get_git_hash()

register.tag(GitHeadHash)


class SettingsFileTimeHash(VersionHashTag):
    """ A template tag that prints an md5 hash
        of the last time the Django settings file
        was accessed """

    name = 'settings_file_time_hash'

    def render_tag(self, context):

        return self.get_atime_hash()


register.tag(SettingsFileTimeHash)







