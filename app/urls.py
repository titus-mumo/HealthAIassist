from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("symptoms-encoding/", views.symptoms_encoding, name="symptoms-encoding"),
    path("login/", views.login_view, name="login"),
    path("get-started/", views.get_started, name='get_started'),
    path("register/", views.register, name="register"),
    path("results/<str:predicted_disease>/", views.results, name="results"),
    path('print-records/', views.print_records, name='print_records'),
    path("user_input/", views.record_user_input, name = 'user_input'),
    path("get_doctor_profiles/", views.get_doctor_profiles, name='get_doctor_profiles'),
    path('doctor_location/<int:doctor_id>/', views.doctor_location, name='doctor_location'),
    path('logout/', views.logout_view, name='logout_view'),
    path('recent_activity/', views.recent_activity, name='recent_activity'),
    path('disease_records/', views.disease_records, name='disease_records'),
    path('feedback/', views.feedback, name ='feedback'),
    path('disease-information/', views.disease_information, name='disease_information'),
    path('all_doctors_location/', views.all_doctors_location, name='all_doctors_location'),
    path('results-loading/', views.loading_page, name='loading_page'),
    path('initialize_stk_push/', views.initialize_stk_push, name='initialize_stk_push'),
    path('settings/', views.settings, name='settings'),
    path('processing/', views.processing, name='processing'),
    path('search_doctor/', views.search_doctor, name='search_doctor'),
    path('locations_viewed/<int:doctor_id>/', views.locations_viewed, name='locations_viewed'),
    
]


