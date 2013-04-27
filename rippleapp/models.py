from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.auth.models import User
from freebase import getFreebaseThing

# Create your models here.



class ripple(models.Model):

	name = models.CharField(max_length = 256)

	class Meta:
		abstract = True

	def __unicode__(self):
		return self.name


class Artist(ripple):
	musicbrainz_id = models.CharField(max_length = 256)
	lastfm_id = models.CharField(max_length = 256)
	soundcloud_id = models.CharField(max_length = 256)
	fb_like_id = models.CharField(max_length = 256)
	fb_page_id = models.CharField(max_length = 256)
	events = models.ManyToManyField('Event', related_name = 'artists')

class Event(ripple):
	lastfm_id = models.CharField(max_length = 256)
	fb_id = models.CharField(max_length = 256)



class fbUser(User):
	user = models.OneToOneField(User, related_name = 'fb_data')
	f_name = models.CharField(max_length=50, unique=True, db_index=True)
	f_id = models.CharField(max_length=50, unique=True, db_index=True)

	location = models.CharField(max_length=80)





