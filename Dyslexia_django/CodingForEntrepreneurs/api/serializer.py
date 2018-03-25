from django.contrib.auth.models import User, Group
from rest_framework import serializers
from questions.models import Question
from patients.models import Patient
from questions.models import Result
from questions.models import Exam
from questions.models import Detailed_Score

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('ques_ID','ques', 'ans1', 'ans2', 'ans3', 'ans4', 'correct_option')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = Patient
        fields = ('patient_ID', 'first_name', 'last_name','age','p_dob','school','grade', 'password', 'p_email')

class PatientCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = Patient
        fields = ('first_name', 'last_name','age','p_dob','school','grade', 'password', 'p_email')
        read_only_fields = ['owner']

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('res_ID', 'exam_ID', 'hits', 'misses', 'accuracy')

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('exam_ID', 'patient_ID')
        
class Detailed_ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detailed_Score
        fields = ('exam_ID', 'ques_ID', 'option_selected')