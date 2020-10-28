from django.db import models

# Create your models here.




class user(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=70)
    tz = models.CharField(max_length=80)

    def __str__(self):
        return self.real_name


class activity(models.Model):
    user_activity = models.ForeignKey(user, related_name='user_activities', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.user_activity

