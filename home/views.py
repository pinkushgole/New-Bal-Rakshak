from django.shortcuts import render, redirect
from .models import ContactUs
from django.contrib import messages

def index(request):
    return render(request, 'home/index.html')

def FAQS(request):
    return render(request, 'home/FAQS.html')

def help_line(request):
    return render(request, 'home/help_line.html')

def mission_vision(request):
    return render(request, 'home/mission_vision.html')

def overview(request):
    return render(request, 'home/overview.html')

def education(request):
    return render(request, 'home/education.html')

def zero_hunger(request):
    return render(request, 'home/zero_hunger.html')

def Medical(request):
    return render(request, 'home/Medical.html')

def contact_us(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        message_text = request.POST.get('message')

        full_name = f"{fname} {lname}".strip()

        # Save in model
        ContactUs.objects.create(
            name=full_name,
            contact=phoneno,
            email=email,
            subject=f"Contact from {full_name} - {phoneno}",
            message=message_text
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact_us')
    return render(request, 'home/contact_us.html')

