from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductFormCreate(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('updated_at', 'owner')

    bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def test_word(self, worddd: str):
        status = 0
        bad_word = ''
        for word in self.bad_words:
            if word.lower() in worddd.lower():
                status = 1
                bad_word = word
                break

        if status == 1:
            raise ValidationError(f"Введено Запрещенное слово '{bad_word}' из списка {self.bad_words}")
        else:
            return worddd

    def clean_name(self):
        name = self.cleaned_data['name']
        return self.test_word(name)

    def clean_description(self):
        desc = self.cleaned_data['description']
        return self.test_word(desc)


class ProductFormUpdate(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'is_publicate',)


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'is_publicate')
