from django.shortcuts import render,redirect
from .models import Review
from .forms import ReviewForm

def create(request):
    if request.method == 'POST':
        data = ReviewForm(request.POST)
        if data.is_valid():
            db_data = data.save(commit=False)
            db_data.user = request.user
            db_data.save()
            return redirect('reviews:index')
    else:
        data = ReviewForm()
    return render(request,'reviews/create.html',{'data':data})

def index(request):
    review = Review.objects.all().order_by('-pk')
    context = {
        'review':review
    }
    return render(request,'reviews/index.html',context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review
    }
    return render(request, 'reviews/detail.html',context)