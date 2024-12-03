from django.db import models

class Laptop(models.Model):
    company = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    typename = models.CharField(max_length=100)
    inches = models.FloatField(null=True)
    ram = models.IntegerField(null=True)
    os = models.CharField(max_length=50)
    weight = models.FloatField(null=True)
    price_euros = models.FloatField()
    screen = models.CharField(max_length=100)
    screen_width = models.FloatField(null=True)
    screen_height = models.FloatField(null=True)
    touchscreen = models.BooleanField(null=True)
    ips_panel = models.BooleanField(null=True)
    retina_display = models.BooleanField(null=True)
    cpu_company = models.CharField(max_length=100, null=True)
    cpu_freq = models.FloatField(null=True)
    cpu_model = models.CharField(max_length=100)
    primary_storage = models.CharField(max_length=100)
    secondary_storage = models.CharField(max_length=100, null=True)
    primary_storage_type = models.CharField(max_length=50, null=True)
    secondary_storage_type = models.CharField(max_length=50, null=True)
    gpu_company = models.CharField(max_length=100)
    gpu_model = models.CharField(max_length=100)
    nome = models.CharField(max_length=100, default='Desconhecido')  # Defina um valor padrão aqui


    def __str__(self):
        return f"{self.product} by {self.company}"