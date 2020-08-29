from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
CITIES = (
    ('KF','Kanifing'),
    ('BR','Brikama'),
    ('BJ','Banjul'),
    ('SK','Serrekunda'),
    ('BA','Basse'),
    ('SM','Soma'),
    ('KR', 'Kaur'),
    ('FF','Farafenni'),
    ('KW','Kerewan'),
    ('FT','Fototo'),
    ('AL', 'Amdalai'),
    ('BAA', 'Bara'),
    ('MK', 'MansaKonko'),
    ('BS','Bansang')
)
class Bus(models.Model):
    bus_no = models.CharField(max_length = 5)
    from_city = models.CharField(max_length = 100, choices=CITIES)
    to_city = models.CharField(max_length=100, choices = CITIES)
    no_of_seats = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    
    def get_absolute_url(self):
        return reverse("reserve", kwargs={"id": self.id})
    
    def __str__(self):
        return self.bus_no
    class Meta:
        verbose_name_plural = 'Buses'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete = models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    email = models.EmailField(blank=True, null=True)
    bus_no = models.CharField(max_length = 5)
    from_city = models.CharField(max_length = 100, choices=CITIES)
    to_city = models.CharField(max_length=100, choices = CITIES)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse("cancel", kwargs={"id": self.id})