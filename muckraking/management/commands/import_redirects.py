from django.conf import settings
from django.core.management.base import LabelCommand
from django.contrib.redirects.models import Redirect
import optparse
import csv
import os
from urlparse import urlparse
from django.contrib.sites.models import Site



# A near-straight copy of
# github:richleland/django-cumulus/blob/27a595a/cumulus/management/commands/syncstatic.py
class Command(LabelCommand):

    help = ("Uploads a csv file of url redirects")

    option_list = LabelCommand.option_list + (
        optparse.make_option('-t', '--test-run',
            action='store_true', dest='test_run', default=False,
            help="Performs a test run of the upload."),
    )


    def handle_label(self, csv_file, **options):

        site = self._select_site()

        csv_file = os.path.abspath(os.path.expanduser(csv_file))

        csv_file = open(csv_file)

        reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        for row in reader:

            if len(row) is not 2:
                print "Bad Redirect: %s" % row
                continue

            try:
                old_path = urlparse(row[0]).path
            except:
                print "Couldn't parse %s" % row[0]
                continue

            redirect, created = Redirect.objects.get_or_create(site=site,
                                                                old_path=old_path)

            redirect.new_path = row[1]

            redirect.save()



    def _select_site(self):
        sites = Site.objects.all()

        if sites.count() == 1:
            pk = sites[0].id
        else:
            print "Choose a site:"
            for s in site:
                print "%s - %s" % (site.pk, site.name)

            pk = raw_input("Your choice:")

        return Site.objects.get(pk=int(pk))

