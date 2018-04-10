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
        df = pd.read_csv(os.getcwd()+'/data/'+csvElectionsFileName)

        results = df[['district', 'office', 'total_votes', 'party', 'votes']]
        results = results[results.office != 'President']
        results = results[results.office != 'Senate']

        #change to other
        results = results.replace(to_replace='IND', value='OTH')
        results = results.replace(to_replace='LIB', value='OTH')
        results = results.replace(to_replace='WGR', value='OTH')
        results = results.fillna(value='OTH')
        #print(results)
        #print(results.party.unique())


        #TODO: aggregate votes for each congressional district

        #Create df with just House votes
        cong = results[results.office == 'House']

        #For each district sum republican votes and add to total votes
        for district in cong.district.unique():
            cur = cong[cong.district == district]

            other_votes = 0
            blue_votes = 0
            red_votes = 0
            total_votes = 0
            red = cur[cur.party == 'REP']
            for row in red.itertuples():
                red_votes += getattr(row, 'votes')

            blue = cur[cur.party == 'DEM']
            for row in blue.itertuples():
                blue_votes += getattr(row, 'votes')

            other = cur[cur.party == 'OTH']
            for row in other.itertuples():
                other_votes += getattr(row, 'votes')

            print(district)
            print(red_votes)
            print(blue_votes)
            print(other_votes)
            total_votes = red_votes + blue_votes + other_votes
            print(total_votes) 
            print('/////////////////////')


            #print(cur)
            #print('Votes for district ' + district ' = ' + cur.sum())

        #TODO: aggregate votes for each state senate district
        #TODO: aggregate votes for each state assembly district
        #TODO: add to database

        '''
        with open(os.getcwd()+'/data/'+csvElectionsFileName, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[2]=='President' or row[2]=='Senate':
                    continue
                pre_district = Pre_District(district_name=row[1], district_no=row[3],office=row[2],party=row[5],candidate=row[6],votes=row[7], year=2016)
                pre_district.save()
        '''


    #load the populations of each congressional district
    def loadFedConPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['CON','PERSONS18']]
        #results = results['CON'].replace(' ',np.nan)
        #results = results.dropna(subset=['CON'])
        final = results.groupby('CON').sum()
        print(final)
        for line in final.itertuples():
            print(line)
            cur_dist = getattr(line, 'Index')
            if cur_dist == ' ':
                continue
            cur = Pre_District.objects.get(office__contains='House', district_no=cur_dist)
            cur.population = getattr(line, 'PERSONS18')
            cur.save()
            print(cur)

    #load the populations of state senate districts
    def loadSenPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['SEN','PERSONS18']]
        results['SEN'].replace(' ',np.nan,inplace=True)
        results.dropna(subset=['SEN'], inplace=True)
        final = results.groupby('SEN').sum()
        print(final)

    #load state assembly populations
    def loadStateAsmPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['ASM','PERSONS18']]
        results['ASM'].replace(' ',np.nan,inplace=True)
        results.dropna(subset=['ASM'], inplace=True)
        final = results.groupby('ASM').sum()
        print(final)

loadData.loadElections('2016-11-08_General.csv')
#loadData.loadFedConPops('Wards2017_ED12toED16.csv')
#loadData.loadSenPops('Wards2017_ED12toED16.csv')
#loadData.loadStateAsmPops('Wards2017_ED12toED16.csv')
