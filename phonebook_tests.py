import unittest
import os
import phonebook


filename = 'test_phonebook.pb'


class PhonebookTest(unittest.TestCase):

	
	def setUp(self):
		print "setup called"
		phonebook.create_phonebook(filename)	

	def test_sanity(self):
		data = 1234
		result = phonebook.hello()
		self.assertEqual(result, data)

	def test_add_phonebook(self):
	 	print "test_add_phonebook called"	 		
		phonebook.add_phonebook(phonebook.read_pb(filename),'Alan', '444')
		result = phonebook.lookup_name(phonebook.read_pb(filename),'Alan')
		self.assertEqual(result, 'Alan 444')

	def test_change_name(self):
		print "test_change_name called"
		phonebook.change_name(phonebook.read_pb(filename), 'Alan' '555')
		result = phonebook.lookup_name(phonebook.read_pb(filename), 'Alan')
		self.assertEqual(result, 'Alan 555')

	def test_lookup(self):
		print "test_lookup called"		
		result = phonebook.lookup_name(phonebook.read_pb(filename), 'Alan')
		self.assertEqual(result, 'Alan 555')

	def test_reverse_lookup(self):
		print "test_reverse-lookup called"
		result = phonebook.reverse_lookup(phonebook.read_pb(filename), '555')
		self.assertEqual(result, 'Alan 555')

	def test_remove_name(self):
		""" Not sure how to approach this one. I thought about using the
		 "name is not in the phonebook error" but that feels wrong
		 as the error is not unqiue to this function"""
		pass
	
	def tearDown(self):
		os.unlink(filename)	


 
if __name__ == '__main__':
	unittest.main()   
    
