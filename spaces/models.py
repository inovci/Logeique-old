from chat.models import Room
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from chat.models import Room

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    contact = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="img/avatars/")

    class Meta():
        ordering = ['user', 'contact']

    def __str__(self):
        return f"{self.user} - {self.contact}"

class Proposal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="proposals")
    rent_proposal = models.BigIntegerField(null=True)
    deposit_proposal = models.BigIntegerField(null=True)
    kind_desire = models.CharField(max_length=50, null=True, default=None)
    rooms_number_desire = models.IntegerField(null=True, default=None)
    area_desire = models.CharField(max_length=50 ,null=True, default=None)
    township_desire = models.CharField(max_length=50 ,null=True, default=None)
    
    class Meta():
        ordering = ['client', 'rent_proposal', 'deposit_proposal']

    def __str__(self):
        return f"{self.id} - {self.client}"

class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='landlord')
    contact = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="img/avatars/")
    clients = models.ManyToManyField(Client, related_name="landlords", through="Deal")

    class Meta():
        ordering = ['user', 'contact']

    def __str__(self):
        return f"{self.user} - {self.contact}"

class House(models.Model):
    house_township = models.CharField(max_length=50)
    house_area = models.CharField(max_length=50)
    house_rent = models.IntegerField()
    house_deposit = models.IntegerField()
    house_kind = models.CharField(max_length=50)
    house_rooms_number = models.IntegerField()
    house_available = models.BooleanField()
    house_to_sell = models.BooleanField()
    house_image = models.ImageField(upload_to="img/houses/")
    house_creation_day = models.DateTimeField(default=datetime.now)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name="houses")

    class Meta():
        ordering = ['house_township', 'house_area', 'house_kind', 'house_rooms_number', 'house_rent', 'house_deposit']

    def __str__(self):
        return f"{self.id} - {self.landlord}"

class Deal(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="client_deals"
    )
    landlord = models.ForeignKey(
        Landlord,
        on_delete=models.CASCADE,
        related_name="landlord_deals"
    )
    house = models.ForeignKey(
        House, 
        on_delete=models.CASCADE,
        related_name="house_deals",
        default=None
    )
    room = models.ForeignKey(
        Room, 
        on_delete=models.CASCADE,
        related_name="room_deals",
    )
    concluded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.landlord} - {self.client}"



