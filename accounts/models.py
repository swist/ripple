from django.db import models
from django.contrib.auth.models import User

class fbUser(User):
	user = models.OneToOneField(User, related_name = 'fb_data')
	f_name = models.CharField(max_length=50, unique=True, db_index=True)
	f_id = models.CharField(max_length=50, unique=True, db_index=True)
	f_first_name = models.CharField(max_length=30)
	f_last_name = models.CharField(max_length=30)
	location = models.CharField(max_length=80)