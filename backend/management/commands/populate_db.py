import re

from django.core.management.base import BaseCommand, CommandError

from backend.models import Reviews


class Command(BaseCommand):
    help = 'This command is used to populate database'
    queryset = Reviews.objects.all()

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        with open(options['file'], 'r') as text_file:
            try:
                counter = 0
                input_list = []
                for line in text_file:
                    if re.match(r'.*/\w+:.*', line) and counter < 8:
                        input_list.append(re.split(':', line.strip(), 1)[1])
                        counter += 1
                    else:
                        if counter == 8:
                            review = Reviews.create(input_list)
                            if not self.queryset.filter(product_id=review.product_id, user_id=review.user_id).exists():
                                review.save()
                            input_list = []
                            counter = 0
                        else:
                            pass
            except Exception:
                raise CommandError('File format is not correct')




