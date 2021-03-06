from django.db import models

# These models store data calculated using the library.
class District_Plan(models.Model):
    time_stamp = models.DateField(auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=50, null=True)
    year = models.IntegerField(null=True)
    map_id = models.IntegerField(null=True)
    equal_population = models.IntegerField(null=True)
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
    district_id = models.AutoField(primary_key=True)
    district_no = models.CharField(null=True, max_length=8)
    office = models.CharField(null=True, max_length=64)
    polsby_popper = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    shwartzberg = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    convex_hull_ratio = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    length_width = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    reock = models.DecimalField(null=True, max_digits=5, decimal_places=5)

# These models store data to be used in calculations by the library.
class Pre_District_Plan(models.Model):
    name = models.CharField(max_length=50, null=True)
    year = models.IntegerField(null=True)
    map_id = models.IntegerField(null=True)
    #county_geometries --> hopefully coming soon
    target_population = models.DecimalField(null=True, max_digits=5, decimal_places=5)

class Pre_District(models.Model):
    pre_district_id = models.AutoField(primary_key=True)
    district_no = models.CharField(null=True, max_length=8)
    office = models.CharField(null=True, max_length=64)
    population = models.IntegerField(null=True)
    red_votes = models.CharField(null=True, max_length=32)
    blue_votes = models.CharField(null=True, max_length=32)
    total_votes = models.CharField(null=True, max_length=64)
    year = models.IntegerField(null=True)
    #geometry
