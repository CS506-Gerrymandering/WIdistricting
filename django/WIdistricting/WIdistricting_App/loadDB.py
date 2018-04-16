import csv
import os, sys
import django
from django.conf import settings
import pandas as pd
import numpy as np

sys.path.append("/Users/dylangunther/Documents/GitHub/WisconsinDistrictMap/django/WIdistricting")
sys.path.append("./..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WIdistricting.settings")
django.setup()
from WIdistricting_App.models import Pre_District

class loadData():
    ##expect file to be in /data
    def loadElections(csvElectionsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvElectionsFileName)

        df = df.fillna('IND')
        df = df.replace(to_replace='WGR', value='IND')
        df = df.replace(to_replace='LIB', value='IND')


        house = df.loc[df['office'] == 'House']
        state_asm = df.loc[df['office'] == 'State Assembly']
        state_sen = df.loc[df['office'] == 'State Senate']


        unique_districts = house.district.unique()
        pop_df = loadData.loadFedConPops('Wards2017_ED12toED16.csv')
        for i in unique_districts:
            curr_dis = house.loc[house['district'] == i]
            a = curr_dis.groupby('party').sum()
            dem_votes = 0
            rep_votes = 0
            ind_votes = 0
            try:
                dem_votes = a.votes['DEM']
            except Exception as e:
                #print('no dem\n')
                pass
            try:
                rep_votes = a.votes['REP']
            except Exception as e:
                #print('no rep\n')
                pass
            try:
                ind_votes = a.votes['IND']
            except Exception as e:
                #print('no ind\n')
                pass

            total_votes = dem_votes + rep_votes + ind_votes
            district_no = int(i)
            office = 'House'
            year = 2016

            population = pop_df.PERSONS18[district_no]

            pre_district = Pre_District(district_no=district_no, office=office,
            red_votes=rep_votes, blue_votes=dem_votes, total_votes=total_votes,
            population=population, year=year)
            pre_district.save()
            #print("House District Number: " + str(i))
            #print(a)
            #print('\n')

        unique_districts = state_asm.district.unique()
        pop_df = loadData.loadStateAsmPops('Wards2017_ED12toED16.csv')
        for i in unique_districts:
            curr_dis = state_asm.loc[state_asm['district'] == i]
            a = curr_dis.groupby('party').sum()
            dem_votes = 0
            rep_votes = 0
            ind_votes = 0
            try:
                dem_votes = a.votes['DEM']
            except Exception as e:
                #print('no dem\n')
                pass
            try:
                rep_votes = a.votes['REP']
            except Exception as e:
                #print('no rep\n')
                pass
            try:
                ind_votes = a.votes['IND']
            except Exception as e:
                #print('no ind\n')
                pass

            total_votes = dem_votes + rep_votes + ind_votes
            district_no = int(i)
            office = 'State Assembly'
            year = 2016
            population = pop_df.PERSONS18[district_no]

            pre_district = Pre_District(district_no=district_no, office=office,
            red_votes=rep_votes, blue_votes=dem_votes, total_votes=total_votes,
            population=population, year=year)
            pre_district.save()


        unique_districts = state_sen.district.unique()
        pop_df = loadData.loadSenPops('Wards2017_ED12toED16.csv')
        for i in unique_districts:
            curr_dis = state_sen.loc[state_sen['district'] == i]
            a = curr_dis.groupby('party').sum()
            dem_votes = 0
            rep_votes = 0
            ind_votes = 0
            try:
                dem_votes = a.votes['DEM']
            except Exception as e:
                #print('no dem\n')
                pass
            try:
                rep_votes = a.votes['REP']
            except Exception as e:
                #print('no rep\n')
                pass
            try:
                ind_votes = a.votes['IND']
            except Exception as e:
                #print('no ind\n')
                pass

            total_votes = dem_votes + rep_votes + ind_votes
            district_no = int(i)
            office = 'State Senate'
            year = 2016
            population = pop_df.PERSONS18[district_no]

            pre_district = Pre_District(district_no=district_no, office=office,
            red_votes=rep_votes, blue_votes=dem_votes, total_votes=total_votes,
            population=population, year=year)
            pre_district.save()

    #load the populations of each congressional district
    def loadFedConPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['CON','PERSONS18']]
        results['CON'].replace(' ',np.nan,inplace=True)
        results = results.dropna(subset=['CON'])
        results.CON = pd.to_numeric(results.CON)
        results = results.sort_values(by=['CON'], ascending=True)
        final = results.groupby('CON').sum()
        return final

    #load the populations of state senate districts
    def loadSenPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['SEN','PERSONS18']]
        results['SEN'].replace(' ',np.nan,inplace=True)
        results.dropna(subset=['SEN'], inplace=True)
        results.SEN = pd.to_numeric(results.SEN)
        results = results.sort_values(by=['SEN'], ascending=True)
        final = results.groupby('SEN').sum()
        return final

    #load state assembly populations
    def loadStateAsmPops(csvPopulationsFileName):
        df = pd.read_csv(os.getcwd()+'/data/'+csvPopulationsFileName)
        results = df[['ASM','PERSONS18']]
        results['ASM'].replace(' ',np.nan,inplace=True)
        results.dropna(subset=['ASM'], inplace=True)
        results.ASM = pd.to_numeric(results.ASM)
        results = results.sort_values(by=['ASM'], ascending=True)
        final = results.groupby('ASM').sum()
        return final

loadData.loadElections('2016-11-08_General.csv')
