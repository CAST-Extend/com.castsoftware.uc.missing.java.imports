'''
Created on May 26, 2021

@author: JGD
'''
import cast_upgrade_1_6_5 # @UnusedImport
import unittest
from cast.application.test import run
from cast.application import create_postgres_engine


class TestIntegration(unittest.TestCase):

    def test1(self):
        
        run(kb_name='ppsconfig_local', application_name='PPSConfig', engine=create_postgres_engine(host='localhost', port=2284))


if __name__ == "__main__":
    unittest.main()
