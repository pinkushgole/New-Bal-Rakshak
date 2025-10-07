"""
URL configuration for Bal_Rakshak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from children import views as cv
from NGO import views as NGO
from dashboard import views as dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
 
 

    path('', views.index, name='index'),
    path('FAQS', views.FAQS, name='FAQS'),
    path('help-line', views.help_line, name='help_line'),
    path('mission-vision', views.mission_vision, name='mission_vision'),
    path('overview', views.overview, name='overview'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('education', views.education, name='education'),
    path('zero-hunger', views.zero_hunger, name='zero_hunger'),
    path('Medical', views.Medical, name='Medical'),


    path('add-children-page', cv.add_children_page, name='add_children_page'),
    path('add-children', cv.add_children, name='add_children'),


    path('login-NGO-page', NGO.login_NGO, name='login_NGO_page'),
    path('registration-NGO-page', NGO.registration_NGO, name='registration_NGO_page'),
    path('logout-NGO', NGO.logout_ngo, name='logout_ngo'),
    path('NGO-home', NGO.NGO_home, name='NGO_home'),
    path('NGO-profile-edit', NGO.edit_ngo_profile, name='edit_ngo_profile'),
    path('children-data-sate-vise', NGO.children_by_ngo_state, name='children_by_ngo_state'),



    path('admin-dashboard', dashboard.admin_dashboard, name='admin_dashboard'),
    path('child/delete/<int:child_id>/', dashboard.delete_child, name='delete_child'),
    path('total-NGO', dashboard.AllNGO, name='All_NGO'),
    path('ngo/delete/<int:ngo_id>/', dashboard.delete_ngo, name='delete_ngo'),
    path('total-query', dashboard.contactus_list, name='All_query'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
