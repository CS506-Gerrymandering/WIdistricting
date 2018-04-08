import csv
import os, sys
import django
from django.conf import settings
sys.path.append("/Users/hitesh/projects/WisconsinDistrictMap/django/WIdistricting")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WIdistricting.settings")
django.setup()
from WIdistricting_App.models import Pre_District
class loadData():
    ##expect file to be in /data
    def loadElections(csvElectionsFileName):
        with open(os.getcwd()+'/data/'+csvElectionsFileName, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[2]=='President':
                    continue
                pre_district = Pre_District(district_name=row[3],office=row[2],party=row[5],candidate=row[6],votes=row[7], year=2016)
                pre_district.save()

loadData.loadElections('2016-11-08_General.csv')