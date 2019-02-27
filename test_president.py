#!/usr/bin/env python

import unittest
from president import President
import datetime

class TestPresident(unittest.TestCase):


    def setUp(self):
        self.p = President(1)

    def test_pres_name_george(self):
        self.assertEqual('George', self.p.first_name, "Name is not George")

    def test_last_name_george(self):
        self.assertEqual('Washington', self.p.last_name, "Name is not Washington")

    def test_date_type(self):
        self.assertIsInstance(self.p.term_end_date,datetime.date, "date not right format")


