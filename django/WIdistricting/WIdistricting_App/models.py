from django.db import models

# Create your models here.
class District_Plan(models.Model):
    time_stamp = models.DateField(auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=50, null=True)
    year = models.IntegerField(null=True)
    #map_id =
    #equal_population =
    efficiency_gap = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    mean_median_diff = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    partisan_bias = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    rep_fairness = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    competitiveness = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    split_municipal_count = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    split_county_count = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    district_split_count = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    avg_polsby_popper = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    avg_reock = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    avg_length_width = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    avg_schwartzberg = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    avg_convex_hull = models.DecimalField(null=True, max_digits=5, decimal_places=5)


class District(models.Model):
    district_id = models.IntegerField(primary_key=True)
    polsby_popper = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    shwartzberg = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    convex_hull_ratio = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    length_width = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    reock = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    district_plan = models.ForeignKey(District_Plan, on_delete=models.CASCADE, null=True)