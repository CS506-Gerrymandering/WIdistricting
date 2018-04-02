# from django.test import TestCase
import nose.tools as nt
# Create your tests here.


### This is a dummy tester to make sure that we are communicating w/ teamcity correctly
class testNose():
    def setup(self):
        self.thing = "thing"

    def testThing(self):
        nt.assert_equal(self.thing, "thing")

    def teardown(self):
        self.thing = None