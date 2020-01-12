from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.TextField()
    capital = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.TextField()
    creation_date = models.DateField()
    external = models.BooleanField(default=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    birthday = models.DateField()
    age = models.PositiveIntegerField(null=True)
    internal = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Ticket(models.Model):
    CHOICES = (
        ('n', 'new'),
        ('i', 'in progress'),
        ('p', 'pending'),
        ('c', 'cancel'),
        ('d', 'done')
    )

    title = models.TextField()
    state = models.CharField(max_length=1, choices=CHOICES, null=True, default='n')
    creation_date = models.DateField(null=True)
    content = models.TextField()
    customer = models.ForeignKey(Company, on_delete=models.CASCADE)
    contributor = models.ManyToManyField('Person', blank=True)

    def __str__(self):
        return '%s (%s)' % (self.title, self.customer)
