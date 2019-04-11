# coding: utf-8

from django import forms
from .models import AA


class OrderForm(forms.ModelForm):
    aa_text = forms.CharField(
        max_length=200,
        initial=u'鈴木太郎',        # 初期値
        widget=forms.Textarea(),
    )

    class Meta:
        model = AA
        fields = ('aa_text',)

        widget = {'aa_text': forms.Textarea(attrs={'size': 2})}
