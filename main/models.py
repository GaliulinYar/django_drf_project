from django.db import models
from django.conf import settings

NULLABLE = {
    'null': True,
    'blank': True
}


class Courses(models.Model):
    """Класс курсов для ViewSets"""
    name_courses = models.CharField(max_length=50, verbose_name='Название курсов')
    preview_courses = models.ImageField(upload_to='static/preview', verbose_name='Изображение', **NULLABLE)
    description_courses = models.CharField(max_length=200, verbose_name='Описание курсов')

    def __str__(self):
        return f'{self.name_courses}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Модель уроков для Generic"""
    lesson_name = models.CharField(max_length=250, verbose_name='Наименование урока')
    lesson_description = models.TextField(verbose_name='Описание урока')
    lesson_preview = models.ImageField(upload_to='static/lesson/', verbose_name='Превью', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    # Привязка урока к курсу
    course_lesson = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Название курса откуда урок')

    def __str__(self):
        return f'Урок - {self.lesson_name} из курса {self.course_lesson}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payments(models.Model):
    """Модель платежей"""

    CASH_PAY = 'Оплата наличными'
    NON_CASH_PAY = 'Оплата по безналу'

    WAYS_PAY = (
        (CASH_PAY, 'Налиными'),
        (NON_CASH_PAY, 'Безналом')
    )

    # Привязка к пользователю
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE)
    date_pay = models.TimeField(auto_now_add=True, verbose_name='Время платежа')
    # Привязка оплаты к курсу и уроку
    course_pay = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    lesson_pay = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    # Сумма оплаты
    sum_pay = models.IntegerField(verbose_name='Сумма оплаты')
    # Способ оплаты: наличные или перевод
    way_pay = models.CharField(choices=WAYS_PAY, verbose_name='Вариант оплаты')

    def __str__(self):
        return (f'Платеж {self.owner} за курс {self.course_pay}, '
                f'за урок {self.lesson_pay} на сумму {self.sum_pay}')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
