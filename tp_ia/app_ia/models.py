from django.db import models

class Laptop(models.Model):
    company = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    typename = models.CharField(max_length=100)
    inches = models.FloatField(null=True)  # Pode ser float para valores decimais
    ram = models.IntegerField(null=True)  # Pode ser um valor inteiro
    os = models.CharField(max_length=50)
    weight = models.FloatField(null=True)  # Pode ser float para valores decimais
    price_euros = models.FloatField()  # Preço em euros, normalmente decimal
    screen = models.CharField(max_length=100)
    screen_width = models.FloatField(null=True)
    screen_height = models.FloatField(null=True)
    touchscreen = models.BooleanField(null=True)
    ips_panel = models.BooleanField(null=True)
    retina_display = models.BooleanField(null=True)
    cpu_company = models.CharField(max_length=100, null=True)  # Permite valores nulos
    cpu_freq = models.FloatField(null=True)  # Pode ser float para valores decimais
    cpu_model = models.CharField(max_length=100)
    primary_storage = models.CharField(max_length=100)
    secondary_storage = models.CharField(max_length=100, null=True)
    primary_storage_type = models.CharField(max_length=50, null=True)
    secondary_storage_type = models.CharField(max_length=50, null=True)
    gpu_company = models.CharField(max_length=100)
    gpu_model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product} by {self.company}"