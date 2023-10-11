from django.contrib import admin

from main.models import Courses, Lesson, Payments, Subscription

admin.site.register(Courses)
admin.site.register(Lesson)
admin.site.register(Payments)
admin.site.register(Subscription)
