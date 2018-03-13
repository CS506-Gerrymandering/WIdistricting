from django.db import models

# Create your models here.
class District(models.Model):
    district_id = models.IntegerField(primary_key=True)
    polsby_popper = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    shwartzberg = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    convex_hull_ratio = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    length_width = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    reock = models.DecimalField(null=True, max_digits=5, decimal_places=5)
