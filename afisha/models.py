from django.utils.translation import ugettext_lazy as _
from django.db import models


class Event(models.Model):
    class Meta():
        db_table = 'event'
    name = models.CharField(_(u'name '),max_length=200)
    date = models.DateTimeField(_(u'date'))
    desc = models.TextField(_(u'description'))
    visitors = models.IntegerField(_(u'mount vizitors'),default=0)

    def __unicode__(self):
    	return self.name