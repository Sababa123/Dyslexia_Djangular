from django.db.models import Q
from rest_framework import generics, mixins

from questions.models import Question
from questions.models import Result
from questions.models import Exam
from questions.models import Detailed_Score
from patients.models import Patient


# class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
#     lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
#     serializer_class        = BlogPostSerializer
#     permission_classes      = [IsOwnerOrReadOnly]
#     #queryset                = BlogPost.objects.all()

#     def get_queryset(self):
#         return BlogPost.objects.all()

#     def get_serializer_context(self, *args, **kwargs):
#         return {"request": self.request}

#     # def get_object(self):
#     #     pk = self.kwargs.get("pk")
#     #     return BlogPost.objects.get(pk=pk)

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializer import QuestionSerializer, ExamSerializer, PatientCreateSerializer, ExamSerializer, ResultSerializer, Detailed_ScoreSerializer, PatientSerializer



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class PatientCreateSet(CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)
    
class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
class ExamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class Detailed_ScoreViewSet(viewsets.ModelViewSet):
    queryset = Detailed_Score.objects.all()
    serializer_class =Detailed_ScoreSerializer
    

