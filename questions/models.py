# from django.db import models
# from quizzes.models import Quiz
#
#
# class Question(models.Model):
#     text = models.CharField(max_length=200, verbose_name='Вопрос')
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Тест")
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
#
#     def __str__(self):
#         return f"{self.text}"
#
#     def get_answers(self):
#         return self.answer_set.all()
#
#     class Meta:
#         verbose_name = "Вопрос"
#         verbose_name_plural = "Вопросы"
#
#
# class Answer(models.Model):
#     text = models.CharField(max_length=200, verbose_name='Вариант Ответа')
#     correct = models.BooleanField(default=False, verbose_name="Правильный Ответ")
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
#
#     def __str__(self):
#         return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct} "
#
#     class Meta:
#         verbose_name = 'Ответ'
#         verbose_name_plural = 'Ответы'

from django.db import models
from quizzes.models import Quiz


class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='Вопрос')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Тест")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.text}"

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='Вариант ответа')
    correct = models.BooleanField(default=False, verbose_name='Правильный ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'