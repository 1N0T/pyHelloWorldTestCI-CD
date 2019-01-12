#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from HelloWorld import HelloWorld


class HelloWorldTest(unittest.TestCase):
	def test_greeting(self):
		saludo = HelloWorld()
		self.assertEqual(saludo.message, "Hello World !!!")
		
		
if __name__ == "__main__":
	unittest.main()
	
