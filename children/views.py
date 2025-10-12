from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import ChildrenInfo

def add_children_page(request):
    return render(request, 'home/children_info_add.html')

def add_children(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        person_contact = request.POST.get('person_contact')
        address = request.POST.get('address')
        details = request.POST.get('details')
        img = request.FILES.get('img')

        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        country = request.POST.get('country', 'India')

        child = ChildrenInfo(
            person_name=person_name,
            person_contact=person_contact,
            address=address,
            details=details,
            img=img,
            city=city,
            state=state,
            pincode=pincode,
            country=country
        )
        child.save()
        
        if child.img:
            print("✅ Cloudinary Image URL:", child.img.url)

        # Redirect ya success message bhi de sakte ho
        return render(request, 'home/children_info_add.html', {
            'success': "Child information added successfully!"
        })

    return render(request, 'home/children_info_add.html')