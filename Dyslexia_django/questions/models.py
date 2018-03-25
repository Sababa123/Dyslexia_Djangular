from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Question(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE) #class_instance.model_set.all()
    ques_ID = models.AutoField(primary_key=True)
    ques = models.TextField()
    ans1 = models.CharField(max_length=50, default='')
    ans2 = models.CharField(max_length=50, default='')
    ans3 = models.CharField(max_length=50, default='')
    ans4 = models.CharField(max_length=50, default='')
    correct_option = models.IntegerField()


class Exam(models.Model):
    exam_ID = models.AutoField(primary_key=True)
    patient_ID = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
	
	

class Result(models.Model):
    res_ID = models.AutoField(primary_key=True)
    exam_ID = models.ForeignKey(Exam, on_delete=models.CASCADE)
    hits = models.IntegerField()
    misses = models.IntegerField()
    accuracy = models.FloatField()
		
class Detailed_Score(models.Model):
    exam_ID = models.ForeignKey(Exam, on_delete=models.CASCADE)
    ques_ID = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_selected = models.CharField(max_length=50, default='')
    class Meta:
        unique_together = (('exam_ID', 'ques_ID'),)
	


			
   