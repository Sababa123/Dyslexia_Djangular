from django.urls import path
from questions.views import QcreateView,QDetailView,QListView,QUpdateView 


from . import views
app_name = 'Question'
urlpatterns = [
    
    path(r'view/',QDetailView.as_view(), name='q_view'),
    #path(r'name/',views.question_view, name='q_name'),
    path(r'create/',QcreateView.as_view(), name='q_create'),
    path(r'update/<pk>/',QUpdateView.as_view(), name='q_update'),

   

   

]
