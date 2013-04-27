from django.db import models
from picklefield.fields import PickledObjectField
from freebase import getFreebaseThing

# Create your models here.



class ripple(models.Model):

	name = models.CharField(max_length = 256)
	raw_data = PickledObjectField()


	class Meta:
		abstract = True

	def __unicode__(self):
		return self.name


