from django.shortcuts import render, redirect, get_object_or_404
from children.models import ChildrenInfo 
from NGO.models import NGOInfo
from home.models import ContactUs

def admin_dashboard(request):
    if request.user.is_authenticated: 
        # Saare children ka queryset fetch karo
        children_data = ChildrenInfo.objects.all()  
        
        # Front-end ko context me bhejo
        context = {
            'children': children_data
        }
        return render(request, 'Admin/admin_home.html', context)
    else:
        return redirect('login_NGO_page')

def delete_child(request, child_id):
    if request.user.is_authenticated:
        child = get_object_or_404(ChildrenInfo, id=child_id)
        child.delete()
        return redirect('admin_dashboard')
    else:
        return redirect('login_NGO_page')
    
def AllNGO(request):
        ngos = NGOInfo.objects.exclude(email='admin@gmail.com')
    
        context = {
            'ngos': ngos  # context me bhi updated naam
        }
        return render(request, 'Admin/total_ngo.html', context)

def delete_ngo(request, ngo_id):
    ngo = get_object_or_404(NGOInfo, id=ngo_id)
    ngo.delete()
    return redirect('all_ngo')

def contactus_list(request):
    contacts = ContactUs.objects.all().order_by('-created_at') 
    return render(request, 'Admin/contact_us_list.html', {'contacts': contacts})