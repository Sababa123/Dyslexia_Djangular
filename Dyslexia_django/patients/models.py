from django.db import models
from django.conf import settings
from questions.models import Result


User = settings.AUTH_USER_MODEL

class Patient(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE) #class_instance.model_set.all()
    patient_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    p_dob = models.DateField(default='')
    school = models.CharField(max_length=50, default='')
    grade = models.IntegerField()
    password = models.CharField(max_length=15, default = '')
    p_email = models.EmailField(default = '')

    
    def __str__(self):
        # return self.p_name
        return self.first_name
    
    