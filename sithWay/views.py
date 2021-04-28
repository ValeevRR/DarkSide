from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from sithWay import forms
from sithWay.forms import RecruitForm
from sithWay.models import *


from django.views.generic import ListView

#  Отображение страницы выбора Рекрут/Ситх
def selection_page(request):
    return render(request, 'selection_page.html')


# Отображение страницы регистрации рекрута
def recruit_page(request):
    planets = Planet.objects.all()
    return render(request, 'recruit/add_recruit.html', {'planets_list': planets})


# Проверка и запись данных рекрута; перенаправление на страницу выбора ордена
def recruit_save(request):
    if request.method == 'POST':
        form_recruit = RecruitForm(request.POST)
        if form_recruit.is_valid():
            recruit = form_recruit.save()
            return redirect('sithWay:recruit_test', recruit.id)
        else:
            return redirect('sithWay:recruit_add_page')


# Подготовка записей ответов в бд
def prepare_blank_answers(recruit):
    question_list = get_random_question_list()
    for question in question_list:
        answer = RecruitAnswer(recruit=recruit, question=question)
        answer.save()


# Отображение страницы испытания для созданного рекрута
def recruit_test(request, pk):
    recruit = get_object_or_404(Recruit, id=pk)
    if len(recruit.recruitanswer_set.all()) == 0:
        prepare_blank_answers(recruit)
    if request.method == 'POST':
        formset = forms.AnswerFormSet(request.POST, instance=recruit)
        if formset.is_valid():
            formset.save()
            return redirect('sithWay:selection_page')
    else:
        formset = forms.AnswerFormSet(instance=recruit)
    return render(request, 'recruit/testHandShadow.html', {'formset': formset, 'recruit': recruit})


class SithListView(ListView):
    model = Sith
    template_name = 'sith/sith_list.html'


# def sith_list(request):
#     sith_list = Sith.objects.all()
#     return render(request, 'sith/sith_list.html', {'sith_list': sith_list})


def sith_recruit_list(request, pk_sith):
    recruit_list = Recruit.objects.filter(teacher=None)
    sith = Sith.objects.get(id=pk_sith)
    return render(request, 'sith/sith_recruit_list.html', {'recruit_list': recruit_list, 'sith': sith})


def sith_recruit_detail(request, pk_sith, pk_recruit):
    recruit = Recruit.objects.get(id=pk_recruit)
    answers = recruit.recruitanswer_set.all()
    return render(request, 'sith/recruit_detail.html', {'recruit': recruit, 'answers': answers, 'sith_pk': pk_sith})


def make_hand_shadow(request, pk_sith, pk_recruit):
    sith = Sith.objects.get(id=pk_sith)
    recruit = Recruit.objects.get(id=pk_recruit)
    if recruit.teacher:
        recruit.teacher = None;
        recruit.save()
    else:
        if (sith.recruit_set.all().count() < 3):
            recruit.teacher = sith
            recruit.save()
            send_mail('Shadow Hand Test', 'Вы приняты в ряды Ордена! Твой учитель '+sith.name+'. Он найдет тебя, когда придет время.',
                      'darksidedjango@gmail.com', [recruit.email], fail_silently=False)
    return redirect('sithWay:recruit_detail', pk_sith=sith.id, pk_recruit=recruit.id)

class SithListMoreThanOne(ListView):
    model = Sith
    context_object_name = 'sith_list'
    template_name = 'sith/sith_list.html'

    def get_queryset(self):
        sith_all_list = Sith.objects.all()
        queryset = []
        for sith in sith_all_list:
            if sith.recruit_set.all().count() > 1:
                queryset.append(sith)
        return queryset
# def sith_list_filtered(request):
#     sith_all_list = Sith.objects.all()
#     sith_list = []
#     for sith in sith_all_list:
#         if sith.recruit_set.all().count() > 1:
#             sith_list.append(sith)
#     return render(request, 'sith/sith_list_filtered.html', {'sith_list': sith_list})
