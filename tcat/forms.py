from django import forms
from .models import Tcat, DynamicField
from django.forms import formset_factory
from ckeditor.widgets import CKEditorWidget

class DynamicFieldForm(forms.ModelForm):
    class Meta:
        model = DynamicField
        fields = ('field_title', 'field_value',)

class TcatForm(forms.ModelForm):
    class Meta:
        model = Tcat
        fields = (
            'title',
            'date',
            'location',
            'price',
            'categori',
            'review',
            'image',
        )

        widget = {
            'review': forms.CharField(widget=CKEditorWidget()),
        }

    categori = forms.ChoiceField(choices=[
        ('','카테고리를 선택해주세요'),
        ('뮤지컬','뮤지컬'),
        ('영화','영화'),
        ('콘서트','콘서트'),
        ('전시회','전시회'),
        ('스포츠','스포츠'),
        ('연극','연극'),
        ('테마파크','테마파크'),
        ('항공권','항공권'),
        ('입장권','입장권'),
        ('기타','기타'),
    ])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs['class'] = 'contents__title--input'
        self.fields['location'].widget.attrs['class'] = 'contents__title--input'
        self.fields['price'].widget.attrs['class'] = 'contents__title--input'
        self.fields['categori'].widget.attrs['class'] = 'contents__title--input'


DynamicFieldFormSet = formset_factory(DynamicFieldForm, extra=1, max_num=5)

class CreateTcatForm(forms.Form):
    tcat_form = TcatForm()
    dynamic_formset = DynamicFieldFormSet(prefix='dynamic_form')