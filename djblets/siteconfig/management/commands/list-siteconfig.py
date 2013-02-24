import json

from django.core.management.base import NoArgsCommand

from djblets.siteconfig.models import SiteConfiguration


class Command(NoArgsCommand):
    """Lists the site configuration."""
    def handle_noargs(self, **options):
        siteconfig = SiteConfiguration.objects.get_current()

        print json.dumps(siteconfig.settings, indent=2)
