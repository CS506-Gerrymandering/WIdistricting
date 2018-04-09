import csv
import os, sys
import django
from django.conf import settings
import pandas as pd
import numpy as np

#/Users/dylangunther/Documents/GitHub/WisconsinDistrictMap/django/WIdistricting
sys.path.append("/Users/dylangunther/Documents/GitHub/WisconsinDistrictMap/django/WIdistricting")
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

    # PERSONS18 = people who can vote and is row 14
    # ASM = assembly row 7
    # SEN = senate row 8
    # CON = congress and is row 9

    #load the populations of each congressional district
    def loadFedConPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['CON','PERSONS18']]
        results['CON'].replace(' ',np.nan,inplace=True)
        results.dropna(subset=['CON'], inplace=True)
        final = results.groupby('CON').sum()

    #load the populations of state senate districts
    def loadSenPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['SEN','PERSONS18']]
        results['SEN'].replace(' ',np.nan,inplace=True)
        results.dropna(subset=['SEN'], inplace=True)
        final = results.groupby('SEN').sum()
        print(final)

    def loadStateAsmPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['ASM','PERSONS18']]
        results['ASM'].replace(' ',np.nan,inplace=True)
        results.dropna(subset=['ASM'], inplace=True)
        final = results.groupby('ASM').sum()
        print(final)

loadData.loadElections('2016-11-08_General.csv')
loadData.loadFedConPops('Wards2017_ED12toED16.csv')
loadData.loadSenPops('Wards2017_ED12toED16.csv')
loadData.loadStateAsmPops('Wards2017_ED12toED16.csv')
