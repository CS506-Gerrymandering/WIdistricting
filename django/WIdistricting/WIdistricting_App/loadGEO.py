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


sys.path.append("./..")
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
	office = 'State Assembly'


	for feature in layer:

	# feature field one is the district ID
		ida = feature['District_N']
	# the feature's geometry
		geom = feature.GetGeometryRef()
		geometry = geom.Clone()
		print(ida)
		pre_districts = Pre_District.objects.filter(district_no=int(ida), office__contains='Assembly').values('population')
		district_plan.append(D(id=int(ida), geometry=geometry, population=pre_districts[0]['population']))

	total_polsby_popper = 0
	total_sch = 0
	total_hull = 0
	## Django Stuff
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

	equi_pop = districts_in_percent_deviation(district_plan, 10.0)
	district_plan_model = District_Plan(name=office, year=2016, avg_polsby_popper=avg_polsby, avg_schwartzberg=avg_sch, 
		avg_convex_hull=avg_hull, equal_population=equi_pop)
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
	office = 'State Senate'

	for feature in layer:

	    # feature field one is the district ID
	    ida = feature['SEN_NUM']
	    print(ida)
	    # the feature's geometry
	    geom = feature.GetGeometryRef()
	    geometry = geom.Clone()
	    pre_districts = Pre_District.objects.filter(district_no=int(ida), office__contains='Senate').values('population')
	    if len(pre_districts) == 1:
	    	district_plan.append(D(id=int(ida), geometry=geometry, population=pre_districts[0]['population']))
	    else:
	    	district_plan.append(D(id=int(ida), geometry=geometry))

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
	equi_pop = districts_in_percent_deviation(district_plan, 10.0)
	district_plan_model = District_Plan(name=office, year=2016, avg_polsby_popper=avg_polsby, avg_schwartzberg=avg_sch, 
		avg_convex_hull=avg_hull, equal_population=equi_pop)
	district_plan_model.save()



def us_house(filename):
	shape_file = filename
	driver = ogr.GetDriverByName('ESRI Shapefile')

	data_source = driver.Open(shape_file, 0)

	if data_source is None:
	    print ("Open failed.\n")
	    sys.exit( 1 )


	layer = data_source.GetLayer()
	layer.ResetReading()

	district_plan = []
	office = 'House'


	for feature in layer:

	    # feature field one is the district ID
	    ida = feature['DISTRICT']
	    # the feature's geometry
	    geom = feature.GetGeometryRef()
	    geometry = geom.Clone()
	    pre_districts = Pre_District.objects.filter(district_no=int(ida), office__contains='House').values('population')
	    district_plan.append(D(id=int(ida), geometry=geometry, population=pre_districts[0]['population']))


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

	equi_pop = districts_in_percent_deviation(district_plan, 10.0)
	district_plan_model = District_Plan(name=office, year=2016, avg_polsby_popper=avg_polsby, avg_schwartzberg=avg_sch, 
		avg_convex_hull=avg_hull, equal_population=equi_pop)
	district_plan_model.save()

if __name__ == "__main__":
	state_assembly('data/shapefiles/state_asm/Wisconsin_State_Assembly_Districts.shp') 
	state_senate('data/shapefiles/state_senate/Wisconsin_Senate_Districts_2011.shp')
	us_house('data/shapefiles/us_house/WI5.shp')