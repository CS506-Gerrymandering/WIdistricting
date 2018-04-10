# from django.test import TestCase
import nose.tools as nt
# Create your tests here.
from WIdistricting_App.models import Pre_District
import csv
import os
import random

# This is a dummy tester to make sure that we are communicating w/ teamcity correctly
class testNose():
    def setup(self):
        self.thing = "thing"

    def testThing(self):
        nt.assert_equal(self.thing, "thing")

    def teardown(self):
        self.thing = None

class testElectionData():
    def setup(self):
        self.electionFileName = '2016-11-08_General.csv'
        self.electionPath = os.getcwd()+'/WIdistricting_App/data/' + self.electionFileName
        #with open(self.electionPath, 'r') as csvFile:
        #    self.file = csvFile

    def testElectionData(self):
        ## testing to verify that data integrity has been preserved
        # 107658 rows in the CSV including the first row which is the key
        probTested = .05 #test 5% of samples
        with open(self.electionPath, 'r') as csvFile:
            reader = csv.reader(csvFile)
            counter = 0
            for row in reader:
                counter += 1
                if(counter > 1 and random.randint(0, 100) * probTested <= 5):
                    district = Pre_District(district_no=row[3], office=row[2], party=row[5],  year=2016)
                    if(district.office is 'President'):
                        continue
                    district_number = row[3]
                    office=row[2]


                    #print(district_number == district.district_name)

                    nt.assert_almost_equal(district_number, district.district_no, None, "Testing District Number Integrity",None)
                    nt.assert_almost_equal(office, district.office, None, "Testing to make sure Candidate is equal", None)

    
    def testElectionDataAPI(self):
        nt.assert_true(False, "The Test Exists")
    
    def teardown(self):
        self.electionFileName = None
        self.electionPath = None
        self.file = None
    
