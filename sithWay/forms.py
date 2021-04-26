from django import forms
from django.forms import inlineformset_factory
from sithWay.models import Recruit, RecruitAnswer


AnswerFormSet = inlineformset_factory(Recruit, RecruitAnswer, exclude=('question',),
        extra=0, can_delete=False)

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ('name', 'age', 'planet', 'email')


class RecruitAnswerForm(forms.ModelForm):
    class Meta:
        model = RecruitAnswer
        fields = ('answer', 'question', 'recruit')
