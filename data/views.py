from django.shortcuts import redirect, render
from django.contrib import messages
import random
from data.forms import addRestaurant, addReview
from data.models import Restaurant, RestaurantReview
from account.models import Account

# Create your views here.
def add_restaurant(request):
    if request.method == "POST":
        form = addRestaurant(request.POST)
        print(form)
        if form.is_valid():
            form.save(commit=False)
            form.sentiment = random.randint(0, 1)
            form.save()
            messages.success(request, 'Restaurant added successfully!')
            return redirect('home')
        else:
            messages.error(request, "Error, Failed to add restaurant!")
    else:
        form = addRestaurant()
    return render(request, "add_restaurant.html", {'form': form})


    return redirect('home')

def list_restaurant(request):
    queryset = Restaurant.objects.all()
    form2 = addRestaurant()
    context = {
        'form' : queryset,
        'form2': form2
    }     
    return render(request, "list_restaurant.html", context)

def add_review(request):
    if request.method == "POST":
        review = addReview(request.user, request.POST)
        if review.is_valid():
            form = review.save(commit=False)
            form.user = Account.objects.get(account_id=request.user)
            form.save()
            messages.success('Review Added Successfully')
        else:
            messages.error('There is something wrong with the submission')
    
    else:
        form = addReview()
    return render(request, "add_review.html", {"form": form})

def list_review(request):
    queryset = RestaurantReview.objects.all()
    context = {
        'form' : queryset
    }
    return render(request, "list_review.html", context)

def edit_restaurant(request, event_id):
    event = Restaurant.objects.get(pk=event_id)
    if request.method == "POST":
        form = addRestaurant(request.POST, instance=event)
        if form.is_valid():
            form.save
            messages.success(request, "Successfully update Restaurant details!")
            return redirect('list_restaurant', event_id)
        else:
            form = addRestaurant(instance=event)
        
    context = {
        'form': form
    }   

    return render(request, 'list_restaurant.html', context)