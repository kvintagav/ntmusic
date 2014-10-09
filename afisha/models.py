from django.utils.translation import ugettext_lazy as _
from django.db import models


class Event(models.Model):
    class Meta():
        db_table = 'event'
    event_name = models.CharField(
        _(u'Name '),
        max_length=200)
    event_date = models.DateTimeField(_(u'date'))
    event_desc = models.TextField(_(u'description'))
    event_visitors = models.IntegerField(_(u'mount vizitors'),default=0)
