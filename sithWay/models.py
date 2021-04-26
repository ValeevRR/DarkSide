from random import randint

from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=30, verbose_name="Планета")

    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = " Планеты"


class Sith(models.Model):
    name = models.CharField(max_length=40, verbose_name="Имя ситха")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name="Планета обучения")

    class Meta:
        verbose_name = "Ситх"
        verbose_name_plural = "Ситхи"


class Recruit(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя рекрута")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name="Планета обитания")
    age = models.SmallIntegerField(verbose_name="Возраст рекрута")
    email = models.EmailField(verbose_name="EMail рекрута")
    teacher = models.ForeignKey(Sith, on_delete=models.CASCADE, verbose_name="Планета обитания", blank=True, null=True)

    class Meta:
        verbose_name = "Рекрут"
        verbose_name_plural = "Рекруты"


class OrderTest(models.Model):
    order = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "Орден испытания"
        verbose_name_plural = "Ордены испытания"


class TestQuestion(models.Model):
    order = models.ForeignKey(OrderTest, on_delete=models.CASCADE)
    question = models.TextField(verbose_name="Вопрос испытания")
    answer = models.BooleanField(verbose_name="Правильный ответ")

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('order',)
        verbose_name = "Вопрос испытания"
        verbose_name_plural = "Воспросы испытания"


def get_random_question_list():
    random_order = randint(1, OrderTest.objects.count())
    return TestQuestion.objects.filter(order=random_order)


class RecruitAnswer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, verbose_name="Рекрут")
    answer = models.BooleanField(verbose_name="Ответ", blank=True,null=True)
    question = models.ForeignKey(TestQuestion, models.CASCADE, verbose_name="Вопрос")

    class Meta:
        verbose_name = "Ответ рекрута"
        verbose_name_plural = "Ответы рекрутов"

    def __str__(self):
        return self.question
