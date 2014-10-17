from django.utils.translation import ugettext_lazy as _
from django.db import models


class Review(models.Model):
	class Meta:
		db_table='review'
	authot = models.CharField(_(u'author'), max_length=200)
	email = models.CharField(_(u'email'), max_length=200)
	text = models.CharField(_(u'text'))
	like = models.InegerField(_(u'like'), default= 0 )
	 
# Create your models here.
