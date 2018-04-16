import sys
import os
from libdistrict.district import District as D
from libdistrict.compactness import polsby_popper, schwartzberg, convex_hull_ratio
from libdistrict.equal_population import districts_in_percent_deviation
from osgeo import gdal, ogr
import django
from django.conf import settings
import pandas as pd
import numpy as np
sys.path.append("/home/shreya/School/506/WisconsinDistrictMap/django/WIdistricting")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WIdistricting.settings")
django.setup()
from WIdistricting_App.models import District, Pre_District, District_Plan


## State Assembly Parsing

def state_assembly(filename):
	shape_file = filename

	driver = ogr.GetDriverByName('ESRI Shapefile')

	data_source = driver.Open(shape_file, 0)

	if data_source is None:
		print ("Open failed.\n")
		sys.exit( 1 )

	layer = data_source.GetLayer()
	layer.ResetReading()

	district_plan = []

	for feature in layer:

	# feature field one is the district ID
		ida = feature.GetField(1)
	# the feature's geometry
		geom = feature.GetGeometryRef()
		geometry = geom.Clone()
		district_plan.append(D(id=int(ida), geometry=geometry))

	total_polsby_popper = 0
	total_sch = 0
	total_hull = 0
	## Django Stuff
	office = 'State Assembly'
	for district in district_plan:

		polsby_popper_score = polsby_popper(district)
		sch_score = schwartzberg(district)
		hull_score = convex_hull_ratio(district)
		total_polsby_popper = total_polsby_popper + polsby_popper_score
		total_sch = total_sch + sch_score
		total_hull = total_hull + hull_score

		district_model = District(district_no=district.id, office=office, polsby_popper=polsby_popper_score, 
			shwartzberg=sch_score, convex_hull_ratio=hull_score)
		district_model.save()

	#district plan
	avg_polsby = total_polsby_popper/99.0
	avg_sch = total_sch/99.0
	avg_hull = total_hull/99.0

	district_plan_model = District_Plan(name=office, year=2016, avg_polsby_popper=avg_polsby, avg_schwartzberg=avg_sch, 
		avg_convex_hull=avg_hull)
	district_plan_model.save()

## State Senate Parsing

def state_senate(filename):
	shape_file = filename
	print("STATE SENATE")
	driver = ogr.GetDriverByName('ESRI Shapefile')

	data_source = driver.Open(shape_file, 0)

	if data_source is None:
	    print ("Open failed.\n")
	    sys.exit( 1 )

	print("2")

	layer = data_source.GetLayer()
	layer.ResetReading()

	district_plan = []

	for feature in layer:

	    # feature field one is the district ID
	    ida = feature.GetField(1)
	    print(ida)
	    # the feature's geometry
	    geom = feature.GetGeometryRef()
	    geometry = geom.Clone()
	    district_plan.append(D(id=int(ida), geometry=geometry))


	office = 'State Senate'

	total_polsby_popper = 0
	total_sch = 0
	total_hull = 0

	for district in district_plan:
		polsby_popper_score = polsby_popper(district)
		sch_score = schwartzberg(district)
		hull_score = convex_hull_ratio(district)
		total_polsby_popper = total_polsby_popper + polsby_popper_score
		total_sch = total_sch + sch_score
		total_hull = total_hull + hull_score
		district_model = District(district_no=district.id, office=office, polsby_popper=polsby_popper_score, 
			shwartzberg=sch_score, convex_hull_ratio=hull_score)

		district_model.save()
	
	#district plan 
	avg_polsby = total_polsby_popper/33.0
	avg_sch = total_sch/33.0
	avg_hull = total_hull/33.0

	district_plan_model = District_Plan(name=office, year=2016, avg_polsby_popper=avg_polsby, avg_schwartzberg=avg_sch, 
		avg_convex_hull=avg_hull)
	district_plan_model.save()



def us_house(filename):
	shape_file = filename
	print("HOUSE")
	driver = ogr.GetDriverByName('ESRI Shapefile')

	data_source = driver.Open(shape_file, 0)

	if data_source is None:
	    print ("Open failed.\n")
	    sys.exit( 1 )


	layer = data_source.GetLayer()
	layer.ResetReading()

	district_plan = []

	for feature in layer:

	    # feature field one is the district ID
	    ida = feature['DISTRICT']
	    # the feature's geometry
	    geom = feature.GetGeometryRef()
	    geometry = geom.Clone()
	    
	    district_plan.append(D(id=int(ida), geometry=geometry))


	office = 'House'
	total_polsby_popper = 0
	total_sch = 0
	total_hull = 0


	for district in district_plan:
		polsby_popper_score = polsby_popper(district)
		sch_score = schwartzberg(district)
		hull_score = convex_hull_ratio(district)
		total_polsby_popper = total_polsby_popper + polsby_popper_score
		total_sch = total_sch + sch_score
		total_hull = total_hull + hull_score

		district_model = District(district_no=district.id, office=office, polsby_popper=polsby_popper_score, 
			shwartzberg=sch_score, convex_hull_ratio=hull_score)

		district_model.save()

		#district plan 
	avg_polsby = total_polsby_popper/8.0
	avg_sch = total_sch/8.0
	avg_hull = total_hull/8.0

	district_plan_model = District_Plan(name=office, year=2016, avg_polsby_popper=avg_polsby, avg_schwartzberg=avg_sch, 
		avg_convex_hull=avg_hull)
	district_plan_model.save()

if __name__ == "__main__":
	state_assembly('data/shapefiles/state_asm/tl_2014_55_sldl.shp') 
	state_senate('data/shapefiles/state_senate/tl_2014_55_sldu.shp')
	us_house('data/shapefiles/us_house/WI5.shp')