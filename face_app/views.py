from django.shortcuts import render, redirect
import time
from .models import User, UserManager, Admin, AdminManager
from os import walk
import os
from django.contrib import messages
import cv2
import random
import shutil
from subprocess import call
import sys

# Create your views here.
def index(request):
    lst = os.listdir('face_app/static/temp_img')
    if len(lst) == 0:
        if 'error_count' in request.session:
            request.session['error_count'] = 0
        lst = os.listdir('face_app/static/temp_img')
        context = {
            'text': 'Take Picture',
            'img': False,
            'range': range(5),
            'count': len(lst),
        }
        return render(request, 'picture.html', context)
    else:
        if 'error_count' in request.session:
            request.session['error_count'] = 0
        context = {
            'text': 'Retake Picture',
            'img': True,
            'range': range(5),
        }
        return render(request, 'picture.html', context)
        
        
def sign_in(request, pic_id):
    lst = os.listdir('face_app/static/temp_img')
    if len(lst) == 0:
        return redirect('/')
    else:
        context ={
            "img": f'face_app/static/temp_img/img{pic_id}.png'
        }
        return render(request, 'login.html', context)

def take_picture(request):
    try:
        call(['python3', 'face_detection_project/face.py'], shell=False, timeout=15)
    except:
        return redirect('/')

def user_process(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/login_errors')
    else:
        rand = random.uniform(1,100)
        shutil.move(request.POST['img'], f'face_app/static/img/{rand}.png')
        img_path = f'/static/img/{rand}.png'
        User.objects.create_user(request.POST, img_path)
    return redirect('/thank_you')

def logout_process(request):
    errors = User.objects.logout_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/logout_errors')
    else:
        user = User.objects.get(username=request.POST['username'])
        user.delete()
        return redirect('/nice_day')

def logout_errors(request):
    if 'error_count' not in request.session:
        request.session['error_count'] = 1
    else:
        request.session['error_count'] += 1
    
    if request.session['error_count'] == 3:
        return redirect('/see_security')
    return render(request, 'logout_errors.html')

def see_security(request):
    request.session.clear()
    return render(request, 'see_security.html')

def logout(request):
    lst = os.listdir('face_app/static/temp_img')
    if len(lst) > 0:
        for i in range(5):
            try:
                os.remove(f'face_app/static/temp_img/img{i}.png')
            except:
                continue
        return render(request, 'logout.html')
    else:
        return render(request, 'logout.html')

def thank_you(request):
    for i in range(5):
        try:
            os.remove(f'face_app/static/temp_img/img{i}.png')
        except:
            continue
    context={
        'user': User.objects.last()
    }
    return render(request, 'thank_you.html', context)

def nice_day(request):
    return render(request, 'nice_day.html')

def admin_login(request):
    errors = Admin.objects.admin_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login_errors')
    else:
        lst = os.listdir('face_app/static/temp_img')
        if len(lst) == 1:
            for i in range(5):
                os.remove(f'face_app/static/temp_img/img{i}.png')
            context = {
                'admin': Admin.objects.get(id=1),
                'all_users': User.objects.all(),
            }
            return render(request, 'security.html', context)
        else:
            context = {
            'admin': Admin.objects.get(id=1),
            'all_users': User.objects.all(),
            }
            return render(request, 'security.html', context)

def login_errors(request):
    return render(request, 'login_errors.html')