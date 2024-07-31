# from django.db import models
# from quizzes.models import Quiz
# from django.contrib.auth.models import User
#
#
# class Result(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Тест")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
#     score = models.FloatField(verbose_name="Балл")
#
#     def __str__(self):
#         return f"{self.pk}"
#
#     class Meta:
#         verbose_name = 'Результат'
#         verbose_name_plural = 'Результаты'

from django.db import models
from quizzes.models import Quiz
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    score = models.FloatField(verbose_name="Балл")

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
