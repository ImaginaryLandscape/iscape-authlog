import sys
import csv
import unicodedata
from django.core.management.base import BaseCommand, CommandError
from authlog.models import Access

CSV_HEADERS=['login_time', 'ip_address', 'ip_forward', 'user', 'path_info', 'user_agent',
             'get_data', 'post_data', 'http_accept', ]

class Command(BaseCommand):
    args = 'None'
    help = 'Dump the Authentication Log to stdout in CSV format.'

    def safe_unicode(self, input_string):
        return unicode(unicodedata.normalize('NFKD',input_string).encode('ascii','ignore'))

    def handle(self, *args, **options):

        csv_writer = csv.writer(sys.stdout)
        csv_writer.writerow(CSV_HEADERS)
        for record in Access.objects.all():
            csv_writer.writerow([
                record.login_time,                                
                self.safe_unicode(record.ip_address),
                self.safe_unicode(record.ip_forward),
                self.safe_unicode(record.user),
                self.safe_unicode(record.path_info),
                self.safe_unicode(record.user_agent),
                self.safe_unicode(record.get_data),
                self.safe_unicode(record.post_data),
                self.safe_unicode(record.http_accept),
            ])
