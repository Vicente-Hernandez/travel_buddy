from django.contrib import messages
from django.db.models import Count
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import redirect, render
#import bcrypt
from .decorators import login_required
from main.models import User, Travel


def index(request):
    return redirect('/login')

def home(request):
    user = request.session['user']
    userid = request.session['user']['id']

    return render(request, 'home.html')






