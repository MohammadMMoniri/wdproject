from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=31, blank=False, verbose_name="نام")


class Ticket(models.Model):
    source = models.CharField(max_length=31, blank=False, verbose_name="نام مبدا")
    destination = models.CharField(max_length=31, blank=False, verbose_name="نام مقصد")
    create_date = models.DateField(null=True, blank=True, verbose_name="تاریخ ایجاد")
    last_update = models.DateTimeField(null=True, blank=True)
    company = models.ForeignKey(
        Company, related_name="tickets", null=True, on_delete=models.SET_NULL
    )
    price = models.IntegerField(null=True, blank=True, verbose_name="قیمت")
    flight_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.source} - {self.create_date}"
