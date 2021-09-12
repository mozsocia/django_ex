from django import forms
from .models import Book, Author
from django.forms.models import inlineformset_factory


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'number_of_pages'
        )


BookFormSet = inlineformset_factory(
    Author,
    Book,
    BookForm,
    can_delete=False,
    min_num=2,
    extra=0
)
