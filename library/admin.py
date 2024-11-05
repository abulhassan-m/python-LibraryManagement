# library/admin.py
from django.contrib import admin
from .models import Book, Member, BorrowRecord

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BorrowRecord)
