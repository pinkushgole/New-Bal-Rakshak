from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import NGOInfo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from children.models import ChildrenInfo



def login_NGO(request):
    if request.method == 'POST':
        email = request.POST.get('ngo_email')
        password = request.POST.get('ngo_password')

        # Authenticate using custom user model
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            # Redirect based on email
            if user.email == "admin@gmail.com":
                return redirect('admin_dashboard')
            else:
                return redirect('NGO_home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login_NGO_page')

    return render(request, 'NGO/NGO_login.html')


def registration_NGO(request):
    if request.method == 'POST':
        name = request.POST.get('ngo_name')
        email = request.POST.get('ngo_email')
        password = request.POST.get('ngo_password')
        contact = request.POST.get('ngo_contact')
        address = request.POST.get('ngo_location')
        img = request.FILES.get('bing')

        ngo = NGOInfo(
            name=name,
            email=email,
            contact=contact,
            address=address,
            img=img,
            password=make_password(password)
        )
        ngo.save()
        return render(request, 'NGO/NGO_registration.html')

    return render(request, 'NGO/NGO_registration.html')

def NGO_home(request):
    if request.user.is_authenticated:
        ngo = request.user 
        return render(request, 'NGO/NGO_home.html', {'ngo': ngo})
    else:
        return redirect('login_NGO_page')

def logout_ngo(request):
    logout(request)
    return redirect('index')



@login_required
def edit_ngo_profile(request):
    ngo = request.user

    if request.method == 'POST':
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        img = request.FILES.get('img')

        if contact:
            ngo.contact = contact
        if address:
            ngo.address = address
        if img:
            ngo.img = img
        ngo.save()
        return redirect('NGO_home')

    return render(request, 'NGO/NGO_edit.html', {'ngo': ngo})


def children_by_ngo_state(request):
    ngo = request.user.id
    if request.user.is_authenticated:
        ngo_state = request.user.state
        children = ChildrenInfo.objects.filter(state=ngo_state)

        context = {
            'children': children,
            'ngo_state': ngo_state
        }
        return render(request, 'NGO/children_list.html', context)
    else:
        return redirect('login_NGO_page')
