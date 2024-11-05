# library/forms.py

from django import forms
from .models import Book, Member, BorrowRecord

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'isbn', 'quantity','stock']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'address', 'contact']
        
class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['book', 'member', 'due_date']
        

