# library/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, BorrowRecord
from django.utils import timezone
from .forms import BookForm, MemberForm, BorrowForm
from datetime import date

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')
    return render(request, 'library/login.html')

def user_logout(request):
    logout(request)
    return redirect('landing_page')

@login_required
def user_dashboard(request):
    return render(request, 'library/user_dashboard.html')

def landing_page(request):
    return render(request, 'library/landing_page.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/update_book.html', {'form': form, 'book': book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'library/delete_book.html', {'book': book})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'library/add_member.html', {'form': form})

# library/views.py

def update_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()  # Save the updated member to the database
            return redirect('member_list')  # Redirect to the member list after updating
    else:
        form = MemberForm(instance=member)  # Populate the form with existing member data

    return render(request, 'library/update_member.html', {'form': form, 'member': member})


def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()  # Delete the member
        return redirect('member_list')
    return render(request, 'library/delete_member.html', {'member': member})


def borrow_book(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            if book.stock > 0:  # Check if the book is available
                borrow_record = form.save(commit=False)
                borrow_record.book = book
                borrow_record.save()
                book.stock -= 1  # Decrement the stock
                book.save()
                return redirect('borrowed_books')  # Redirect to the list of borrowed books
            else:
                form.add_error('book', 'This book is not available.')
    else:
        form = BorrowForm()
    
    return render(request, 'library/borrow_book.html', {'form': form})

def borrowed_books(request):
    borrowed_records = BorrowRecord.objects.filter(return_date__isnull=True)  # Get all borrowed records that haven't been returned
    return render(request, 'library/borrowed_books.html', {'borrowed_records': borrowed_records})

# Return a book
def return_book(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == 'POST':
        borrow_record.return_date = timezone.now()  # Set the return date to now
        borrow_record.book.stock += 1  # Increment the stock
        borrow_record.book.save()
        borrow_record.save()  # Save the updated borrow record
        return redirect('borrowed_books')
    
    return render(request, 'library/return_book.html', {'borrow_record': borrow_record})

# library/views.py

def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)  # Search by title

    return render(request, 'library/book_list.html', {'books': books, 'query': query})

# library/views.py

@login_required
def report(request):
    total_books = Book.objects.count()
    total_members = Member.objects.count()
    total_transactions = BorrowRecord.objects.filter(return_date__isnull=True).count()  # Active borrows

    context = {
        'total_books': total_books,
        'total_members': total_members,
        'total_transactions': total_transactions,
    }
    return render(request, 'library/report.html', context)

def dashboard(request):
    # Calculate counts and get recent transactions
    total_books = Book.objects.count()
    total_members = Member.objects.count()
    books_borrowed = BorrowRecord.objects.filter(return_date__isnull=True).count()
    overdue_books = BorrowRecord.objects.filter(due_date__lt=date.today(), return_date__isnull=True).count()
    recent_transactions = BorrowRecord.objects.order_by('-issue_date')[:10]  # Last 10 transactions

    # Context for template rendering
    context = {
        'total_books': total_books,
        'total_members': total_members,
        'books_borrowed': books_borrowed,
        'overdue_books': overdue_books,
        'recent_transactions': recent_transactions,
        'today': date.today(),
    }
    return render(request, 'library/dashboard.html', context)