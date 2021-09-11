from django.contrib import messages
from django.db.models import Count
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from main.models import User, Travel
from datetime import date

@login_required
def index(request):
    return redirect('/travels')

@login_required
def home(request):
    traveler = User.objects.get(id=request.session['user']['id'])
    travels = Travel.objects.filter(travellers=traveler).all()
    other_travels = Travel.objects.exclude(travellers=traveler).all()
    data = {
        'travels': travels,
        'other_travels': other_travels
    }

    return render(request, 'home.html', data)

@login_required
def abort(request,travel_id):
    user=User.objects.get(id=request.session['user']['id'])
    travel=Travel.objects.get(id=travel_id)
    travel.travellers.remove(user)
    messages.warning(request, "You aborted traveling!")
    return redirect('/travels')

@login_required
def delete(request,travel_id):
    travel=Travel.objects.get(id=travel_id)
    travel.delete()
    messages.warning(request, "You successfully eliminated the trip!")
    return redirect('/travels')

@login_required
def join(request,travel_id):
    user=User.objects.get(id=request.session['user']['id'])
    trip=Travel.objects.get(id=travel_id)
    trip.travellers.add(user)
    messages.success(request, "You successfully joined!")
    return redirect('/travels')

@login_required
def view(request,travel_id):
    travel=Travel.objects.get(id=travel_id)
    context = {
        "travel":travel
    }
    return render(request, 'view.html', context)

@login_required
def add(request):
    if request.method=='GET':
        
        today = date.today().strftime('%Y-%m-%d')
        context = {
            "today":today
        }
        return render(request, 'add.html', context)
    
    if request.method =='POST':
        
        errors = Travel.objects.validador_basico(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/addtrip')
        
        else:    
            destination=request.POST['destination']
            description=request.POST['description']
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            
            
            creator=User.objects.get(id=request.session['user']['id'])
            
            viaje=Travel.objects.create(
                destination=destination,
                description=description,
                start_date=start_date,
                end_date=end_date,
                creator=creator)
            
            viaje.travellers.add(creator)
            
            return redirect('/travels')


