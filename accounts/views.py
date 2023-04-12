from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
from django.http import HttpResponse
import pickle
import numpy as np
import json
# from .forms import NormalUserForm, Hotel, CabDriverForm
from .forms import NormalUserForm, HotelUserForm

model = pickle.load(
    open(r'C:\Users\HP\Downloads\HotelRBS\banglore_home_prices_model.pickle', 'rb'))
__locations = None
__data_columns = None

f = open(r'C:\Users\HP\Downloads\HotelRBS\columns.json')
__data_columns = json.loads(f.read())['data_columns']


def login_view(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass']

        if username == "admin" and password == "admin":
            return redirect('accounts:admin')

        # Check NormalUser
        normal_user = authenticate(username=username, password=password)
        if normal_user is not None:
            login(request, normal_user)
            return redirect('appartment_user_view')

        normal_user2 = NormalUser.objects.filter(
            username=username, password=password).first()
        if normal_user2 is not None:
            login(request, normal_user2)
            request.session['id'] = normal_user2.user_id
            return redirect('accounts:appartment_user_view')

        # Check HotelOwner
        hotel_owner = HotelOwner.objects.filter(
            username=username, password=password).first()
        if hotel_owner is not None:
            login(request, hotel_owner)
            return redirect('accounts:hotel_owner_home')

        # Check CabDriver
        cab_driver = CabDriver.objects.filter(
            username=username, password=password).first()
        if cab_driver is not None:
            login(request, cab_driver)
            return redirect('cab_driver_home')

    return render(request, 'login.html')


def appartment_user_view(request):
    appartments = Appartment.objects.all()
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    return render(request, 'user_appartment.html', {'dis': dis, 'appartments': appartments})


def all_users(request):
    dis = NormalUser.objects.all()
    return render(request, 'all_user.html', {'dis': dis})


def home_view(request):
    __locations = __data_columns[3:]
    if request.method == 'POST':
        input_json = {
            "loca": request.POST['loc'],
            "area": request.POST['area'],
            "bhk": request.POST['bhk'],
            "bath": request.POST['bath']
        }

        result = get_estimated_price(input_json)

        if result > 100:
            result = round(result/100, 2)
            result = str(result) + ' Crore'
        else:
            result = str(result) + ' Lakhs'

        return render(request, 'result.html', {'result': result, 'input_json': input_json})

    return render(request, 'home.html', {'location': __locations})


def get_estimated_price(input_json):
    try:
        loc_index = __data_columns.index(input_json['loca'].lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = input_json['area']
    x[1] = input_json['bath']
    x[2] = input_json['bhk']
    if loc_index >= 0:
        x[loc_index] = 1
    result = round(model.predict([x])[0], 2)
    return result


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    appartments = Appartment.objects.all()
    return render(request, 'about.html', {'appartments': appartments})


def appartment(request):
    return render(request, 'appartment.html')


def normal_user_home(request):
    return render(request, 'home.html')


def hotel_owner_home(request):
    return render(request, 'hotelHome.html')


def cab_driver_home(request):
    return render(request, 'cabHome.html')


def booking(request, name):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    appartments = Appartment.objects.get(appartmentname=name)
    return render(request, 'booking.html',{'dis':dis,'appartments':appartments})


def edit(request, name):
    appartments = Appartment.objects.get(appartmentname=name)
    return render(request, 'edit.html', {'appartments': appartments})


def editbtn(request, name):
    appartments = Appartment.objects.get(appartmentname=name)
    if request.method == 'POST':
        apname = request.POST.get('apname')
        ptype = request.POST.get('ptype')
        adrs = request.POST.get('adrs')
        location = request.POST.get('location')
        zip = request.POST.get('zip')
        yr = request.POST.get('yr')
        ps = request.POST.get('ps')
        nb = request.POST.get('nb')
        nba = request.POST.get('nba')
        fur = request.POST.get('fur')
        ava = request.POST.get('ava')
        price = request.POST.get('price')
        prt = request.POST.get('prt')
        Appartment.objects.filter(appartmentname=name).update(appartmentname=apname, propertytype=ptype, address=adrs, location=location,
                                                           zipcode=zip, year=yr, propertysize=ps, bedrooms=nb,
                                                           bathrooms=nba, furnishing=fur, availability=ava,
                                                           price=price, propdesc=prt)
    return redirect('accounts:admin')


def payment(request):
    return render(request, 'payment.html')

def payments(request):
    return render(request, 'payments.html')


def logout_user(request):
    request.session.flush()
    return redirect('index')


def register_type(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'normal_user':
            return redirect('accounts:register_normal_user')
        elif user_type == 'hotel_owner':
            return redirect('accounts:register_hotel')
        elif user_type == 'cab_driver':
            return redirect('accounts:register_cab_driver')
        else:
            form = None
    else:
        form = None
    context = {
        'form': form
    }
    return render(request, 'registration_type.html', context)


def register_normal_user(request):
    form = NormalUserForm(request.POST or None)
    if form.is_valid():
        acc = NormalUser()
        acc.username = form.cleaned_data['firstname']
        acc.lastname = form.cleaned_data['lastname']
        acc.phone_num = form.cleaned_data['phone']
        acc.email = form.cleaned_data['email']
        acc.password = form.cleaned_data['password1']

        acc.save()
        return redirect('accounts:login')
    context = {
        'form': form
    }
    return render(request, 'register_normal_user.html', context)


def register_hotel_owner(request):
    form = HotelUserForm(request.POST or None)
    if form.is_valid():
        acc = HotelOwner()
        acc.username = form.cleaned_data['firstname']
        acc.lastname = form.cleaned_data['lastname']
        acc.email = form.cleaned_data['email']
        acc.password = form.cleaned_data['password1']

        acc.save()
        return redirect('accounts:login')
    context = {
        'form': form
    }
    return render(request, 'register_hotel_owner.html', context)


def admin(request):
    appartments = Appartment.objects.all()
    return render(request, 'admin.html', {'appartments': appartments})

def search(request):
    if request.method == 'POST':
        loc= request.POST.get('hotelloc')
        loca = Appartment.objects.filter(location=loc)
        return render(request, 'search.html', {'appartments': loca})

def appartments(request):
    if request.method == 'POST':
        apname = request.POST.get('apname')
        ptype = request.POST.get('ptype')
        adrs = request.POST.get('adrs')
        apname = request.POST.get('apname')
        location = request.POST.get('location')
        zip = request.POST.get('zip')
        yr = request.POST.get('yr')
        ps = request.POST.get('ps')
        nb = request.POST.get('nb')
        nba = request.POST.get('nba')
        fur = request.POST.get('fur')
        ava = request.POST.get('ava')
        rent = request.POST.get('rent')
        price = request.POST.get('price')
        img = request.FILES['image']
        prt = request.POST.get('prt')
        ob = Appartment()
        ob.appartmentname = apname
        ob.propertytype = ptype
        ob.address = adrs
        ob.location = location
        ob.zipcode = zip
        ob.year = yr
        ob.propertysize = ps
        ob.bedrooms = nb
        ob.bathrooms = nba
        ob.furnishing = fur
        ob.availability = ava
        ob.rent = rent
        ob.price = price
        ob.cimage = img
        ob.propdesc = prt
        ob.save()
    return redirect('accounts:admin')
