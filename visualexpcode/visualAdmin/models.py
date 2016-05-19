from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class visualUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_date = models.DateField(),
	telephone = models.CharField(max_length=12)

	def __str__(self):
		return self.user.first_name + self.user.last_name

