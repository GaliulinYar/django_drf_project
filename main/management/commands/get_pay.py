from datetime import datetime

from django.core.management import BaseCommand

from main.models import Payments


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Добавляем платежа"""
        date_time_now = datetime.now()

        payment = Payments.objects.create(
            owner=None,
            date_pay=date_time_now,
            course_pay=None,
            lesson_pay=None,
            sum_pay=1000,
            way_pay='Налиными',
        )

        payment.save()
