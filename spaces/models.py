from chat.models import Room
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from chat.models import Room

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='client')
    contact = models.CharField(max_length=50)
    avatar = models.ImageField(
        null=True, blank=True, upload_to="img/avatars/", default="img/avatars/default-user-img.png")

    class Meta():
        ordering = ['user', 'contact']

    def __str__(self):
        return f"{self.user} - {self.contact}"


class Proposal(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="proposals")
    rent_proposal = models.BigIntegerField(null=True)
    deposit_proposal = models.BigIntegerField(null=True)
    kind_desire = models.CharField(max_length=50, null=True, default=None)
    rooms_number_desire = models.IntegerField(null=True, default=None)
    area_desire = models.CharField(max_length=50, null=True, default=None)
    township_desire = models.CharField(max_length=50, null=True, default=None)

    class Meta():
        ordering = ['client', 'rent_proposal', 'deposit_proposal']

    def __str__(self):
        return f"{self.id} - {self.client}"


class Landlord(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='landlord')
    contact = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="img/avatars/")
    clients = models.ManyToManyField(
        Client, related_name="landlords", through="Deal")

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
    landlord = models.ForeignKey(
        Landlord, on_delete=models.CASCADE, related_name="houses")

    class Meta():
        ordering = ['house_township', 'house_area', 'house_kind',
                    'house_rooms_number', 'house_rent', 'house_deposit']

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
        default=None
    )
    concluded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.landlord} - {self.client}"


class ClientFile(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="client_client_files"
    )

    house = models.OneToOneField(
        House,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="house_client_files"
    )

    id_card = models.ImageField(upload_to="img/id_cards/")

    payslip1 = models.ImageField(upload_to="img/payslips/")
    payslip1 = models.ImageField(upload_to="img/payslips/")
    payslip1 = models.ImageField(upload_to="img/payslips/")

    energy_bill1 = models.ImageField(upload_to="img/bills/")
    energy_bill2 = models.ImageField(upload_to="img/bills/")

    last_rent_receipt1 = models.ImageField(upload_to="img/last_rent_receipts/")
    last_rent_receipt2 = models.ImageField(upload_to="img/last_rent_receipts/")

    occupancy_date = models.DateField()

    balance = models.BigIntegerField()

    departure_date = models.DateField(default=datetime.now)
