# from template.file_render import render_data,sanitize,main
from file_render import render_data,sanitize,main
from unittest.mock import patch
import unittest
import os
import sys
from io import StringIO

enabletracemalloc = False

if enabletracemalloc:
	import tracemalloc
	tracemalloc.start()

class TestFileRender(unittest.TestCase):

	def setup(self):
		tt = open("test_template", "w")
		tt.write("""{\n  "var1": "{{ testvar1 }}",\n  "var2": "{{ testvar2 }}" \n}""")
		tt.close()

		td = open("test_data", "w")
		td.write("""testvar1: val1\ntestvar2: val2""")
		td.close()

	def test_render_data(self):
		vardict   = {}
		separator = ":" 
		try:
			self.setup()
			expected_data = """{\n  "var1": "val1",\n  "var2": "val2" \n}"""

			render_data("test_template", "test_data", "outputfile", vardict, separator)
			f = open("outputfile","r")
			data = f.read()
			f.close()
			self.assertEqual(expected_data, data)

		finally:
			os.remove("test_template")
			os.remove("test_data")
			os.remove("outputfile")
			if enabletracemalloc:
				snapshot = tracemalloc.take_snapshot()
				top_stats = snapshot.statistics('lineno')

				print("[ Top 10 ]")
				for stat in top_stats[:10]:
				    print(stat)

	def test_sanitize(self):
		inp = "test;&&123"
		exp = "test123"
		oup = sanitize(inp)
		self.assertEqual(exp, oup)


	def test_main(self):
		try:
			self.setup()
			fake_args = ['main', '-i', 'test_template', '-d', 'test_data', '-o', 'outputfile']
			expected_data = """{\n  "var1": "val1",\n  "var2": "val2" \n}"""

			with patch('sys.argv', fake_args):
				main()
				f = open("outputfile","r")
				data = f.read()
				f.close()
				self.assertEqual(expected_data, data)

		finally:
			os.remove("test_template")
			os.remove("test_data")
			os.remove("outputfile")

	def test_main_vardata_separator(self):
		try:
			self.setup()
			fake_args = ['main', '-i', 'test_template', '-d', 'test_data', '-o', 'outputfile', '-v', 'key:val', '-s', ':']
			expected_data = """{\n  "var1": "val1",\n  "var2": "val2" \n}"""

			with patch('sys.argv', fake_args):

				main()
				f = open("outputfile","r")
				data = f.read()
				f.close()
				self.assertEqual(expected_data, data)

		finally:
			os.remove("test_template")
			os.remove("test_data")
			os.remove("outputfile")

	def test_main_output(self):
		try:
			capturedOutput = StringIO() 	# Create StringIO object
			sys.stdout = capturedOutput             #  and redirect stdout

			self.setup()
			fake_args = ['main', '-i', 'test_template', '-d', 'test_data', '-v', 'key:val', '-s', ':']
			expected_data = """ input file : test_template\n  data file : test_data\noutput file : \n\n******************OUTPUT******************\n\n{\n  "var1": "val1",\n  "var2": "val2" \n}\n"""

			with patch('sys.argv', fake_args):
				main()
				sys.stdout = sys.__stdout__                   # Reset redirect.
				data = capturedOutput.getvalue()
				self.assertEqual(expected_data, data)

		finally:
			os.remove("test_template")
			os.remove("test_data")


	def test_main_help(self):
		try:
			capturedOutput = StringIO() 	# Create StringIO object
			sys.stdout = capturedOutput     #  and redirect stdout

			fake_args = ["main" "-h"]
			expected_data = '[HELP] file_render -i <input file name> -d <data file name> -o <output file name>'

			with self.assertRaises(SystemExit) as cm:
				with patch('sys.argv', fake_args):
					sys.argv= fake_args
					main()
			sys.stdout = sys.__stdout__                   # Reset redirect.
			data = capturedOutput.getvalue()
			# print ('Captured', data, "************1##############333" )
			self.assertEqual(cm.exception.code, 1)
			self.assertEqual(expected_data, data)
		finally:
			pass


if __name__ == '__main__':
	unittest.main()

 # coverage run -m unittest discover -s=test