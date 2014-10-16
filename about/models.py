from django.utils.translation import ugettext_lazy as _
from django.db import models


class Actor(models.Model):
    class Meta():
        db_table = 'actor'
    name_English = models.CharField(_(u'name_English '),max_length=200)
    name = models.CharField(_(u'name '),max_length=200)
    desc = models.TextField(_(u'description'))
    title = models.TextField(_(u'title'))
    chef = models.BooleanField( default = False)

    """изображение"""
    def __unicode__(self):
    	return self.name