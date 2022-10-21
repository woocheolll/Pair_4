from django.shortcuts import render,redirect
from .models import Review
from .forms import ReviewForm

def create(request):
    if request.method == 'POST':
        data = ReviewForm(request.POST)
        if data.is_valid():
            db_data = data.save(commit=False)
            db_data.save()
            return redirect('reviews:index')
    else:
        data = ReviewForm()
    return render(request,'reviews/create.html',{'data':data})
