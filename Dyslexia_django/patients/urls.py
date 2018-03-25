from django.urls import path
from patients.views import contactview,patients_listview,patients_createform,patients_classcreateform,aboutview,patient_UpdateView

from . import views
app_name = 'Patient'
urlpatterns = [
    #path(r'', views.index, name='index'),
    #path(r'contact/', views.contact, name='contact'),
    path(r'view/',views.patients_view, name='patients_view'),
    path(r'name/',views.patients_name, name='patients_name'),
    #path(r'patients/listview',patients_listview.as_view()),
    path(r'<int:p_id>/',views.patients_detailview, name='patients_detail'),
    #path(r'patients/create/',views.patients_createform, name='create_form'),
    path(r'create/',patients_classcreateform.as_view(), name='create_form'),
    path(r'update/<pk>/',patient_UpdateView.as_view(), name='patient_update'),
    
    
   
    #path(r'login/', LoginView.as_view() , name = 'p_log' ),
    
   

]
