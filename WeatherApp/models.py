from django.db import models
from django.utils import timezone

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=25, default="")
    date = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self):
        return self.name
    @property
    def delete_after_1_day(self):
        time = self.date + timezone.timedelta(days=1)
        if time < timezone.now():
            e = City.objects.get(name=self.name)
            e.delete()
            return True
        else:
            return False