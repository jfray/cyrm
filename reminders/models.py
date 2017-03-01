from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify

import datetime
import time_uuid

class Reminder(models.Model):
    publish_date = models.DateTimeField('date published')
    run_date = models.DateTimeField('date to run')
    slug = models.SlugField(unique=True)
    text = models.TextField()

    def save(self, *args, **kwargs):
        trunc_text = self.text[0:15]
        tuuid = time_uuid.TimeUUID.with_utc(datetime.datetime.utcnow())
        slug_to_slugify = "%s-%s" % (trunc_text, tuuid)
        self.slug = slugify(slug_to_slugify)
        super(Reminder, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug
